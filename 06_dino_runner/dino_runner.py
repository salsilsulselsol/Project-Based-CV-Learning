import cv2
import mediapipe as mp
import time
from pynput.keyboard import Key, Controller

# --- Inisialisasi MediaPipe Hands ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=1, 
                       min_detection_confidence=0.7, 
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# --- Inisialisasi Kontroler pynput ---
keyboard = Controller()

# --- Variabel Status (Logika Tap + Cooldown) ---
# Status untuk mencegah tap beruntun
can_jump = True 
cooldown = 0.2
last_action_time = 0

# Akses webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

print("Mulai deteksi (Versi Sederhana). Buka game 'chrome://dino'.")
print("Angkat jari telunjuk 👆 untuk lompat.")
print("Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()
    gesture_detected = "DIAM"

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Logika deteksi jari telunjuk ke atas
        index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        index_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y

        if index_tip_y < index_pip_y:
            gesture_detected = "LOMPAT"
        
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
    # --- Logika Kontrol Keyboard (Tap + Cooldown) ---
    if gesture_detected == "LOMPAT":
        # Jika gestur LOMPAT terdeteksi DAN kita boleh lompat
        if can_jump:
            print("LOMPAT! (Tap Instan)")
            
            # Lakukan press dan release di frame yang SAMA
            # Ini adalah "ketukan" (tap) paling instan yang bisa kita buat
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            
            # Set status bahwa kita baru saja lompat & mulai cooldown
            can_jump = False
            last_action_time = current_time
            
    else: # Jika gestur "DIAM" atau tidak ada tangan
        # Jika kita sedang dalam masa cooldown
        if not can_jump:
            # Cek apakah cooldown sudah lewat
            if current_time - last_action_time > cooldown:
                # Jika sudah, kita siap lompat lagi
                can_jump = True
    # ----------------------------------------------------

    # Tampilkan status di layar
    status_text = "SIAP" if can_jump else "COOLDOWN"
    cv2.putText(frame, f'Status: {status_text}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Dino Runner Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()