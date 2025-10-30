import cv2
import mediapipe as mp

# --- Inisialisasi MediaPipe Hands ---
mp_hands = mp.solutions.hands
# Buat objek 'Hands'. 
# static_image_mode=False -> untuk video
# max_num_hands=2 -> deteksi maksimal 2 tangan
# min_detection_confidence=0.5 -> anggap deteksi berhasil jika > 50% yakin
hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=2, 
                       min_detection_confidence=0.5, 
                       min_tracking_confidence=0.5)

# Inisialisasi utilitas untuk menggambar landmark
mp_drawing = mp.solutions.drawing_utils
# ------------------------------------

# Akses webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

print("Mulai deteksi tangan... Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal membaca frame.")
        break

    # Balik gambar (mirror) agar intuitif
    frame = cv2.flip(frame, 1)

    # --- Proses Deteksi MediaPipe ---
    # 1. Konversi BGR (OpenCV) ke RGB (MediaPipe)
    #    Ini langkah PENTING! MediaPipe dilatih dengan gambar RGB.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 2. Proses gambar dan dapatkan hasilnya
    results = hands.process(rgb_frame)
    # ---------------------------------

    # --- Gambar Hasilnya ---
    # Cek apakah ada tangan yang terdeteksi
    if results.multi_hand_landmarks:
        # Loop untuk setiap tangan yang terdeteksi
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar titik landmark (titik) dan koneksinya (garis)
            mp_drawing.draw_landmarks(
                frame,                  # Gambar target (frame asli BGR)
                hand_landmarks,         # Titik-titik landmark
                mp_hands.HAND_CONNECTIONS # Instruksi cara menyambungkan titik-titik
            )
    # -----------------------

    # Tampilkan frame yang sudah digambar
    cv2.imshow('Hand Tracker - MediaPipe', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Program selesai.")