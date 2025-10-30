import cv2
import mediapipe as mp
import math
import numpy as np

# --- BARU: Impor library untuk kontrol volume ---
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
# -----------------------------------------------

# --- Inisialisasi MediaPipe Hands ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=1, 
                       min_detection_confidence=0.7, 
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# --- BARU & DIPERBAIKI: Setup Kontrol Volume Sistem ---
# 1. Dapatkan perangkat speaker default
devices = AudioUtilities.GetSpeakers()

# 2. Dapatkan antarmuka (interface) EndpointVolume dari perangkat
#    Ini adalah cara yang benar, BUKAN memanggil .Activate()
volume_interface = devices.EndpointVolume

# 3. "Cast" (ubah) antarmuka COM ini menjadi tipe yang bisa dipahami Python
volume = cast(volume_interface, POINTER(IAudioEndpointVolume))

# 4. Dapatkan rentang volume (dalam format dB, misal: -65.0 s.d. 0.0)
vol_range_db = volume.GetVolumeRange()
min_vol_db = vol_range_db[0]
max_vol_db = vol_range_db[1]
# --------------------------------------------------

# Akses webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

print("Mulai deteksi... Gerakkan ibu jari dan telunjuk untuk mengontrol volume.")
print("Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
        index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
        
        distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
        
        # --- Petakan Jarak ke Persentase (Gunakan kalibrasi Anda [28, 230]) ---
        vol_percent = np.interp(distance, [20, 200], [0, 100])
        
        # --- Petakan Persentase ke dB dan Set Volume Sistem ---
        vol_db = np.interp(vol_percent, [0, 100], [min_vol_db, max_vol_db])
        volume.SetMasterVolumeLevel(vol_db, None)
        # -------------------------------------------------------------

        # --- Visualisasi (Bar Hijau & Teks) ---
        bar_height = int(np.interp(vol_percent, [0, 100], [400, 150]))
        cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(frame, (50, bar_height), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, f'{int(vol_percent)} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Visualisasi Jari (opsional)
        cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (index_x, index_y), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), 3)

    cv2.imshow('Gesture Volume Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()