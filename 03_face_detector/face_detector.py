# face_detector.py

import cv2

# Muat classifier untuk WAJAH
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# --- BARU: Muat classifier untuk MATA ---
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Cek apakah classifier berhasil dimuat
if face_cascade.empty() or eye_cascade.empty():
    print("Error: Tidak bisa memuat satu atau lebih file cascade classifier (.xml).")
    print("Pastikan 'haarcascade_frontalface_default.xml' dan 'haarcascade_eye.xml' ada.")
    exit()

# Akses webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

print("Webcam terbuka. Mencari wajah dan mata... Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Tidak bisa menerima frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah (gunakan nilai minNeighbors yang cocok untuk Anda, misal 3)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    # Loop melalui setiap wajah yang terdeteksi
    for (x, y, w, h) in faces:
        # Gambar kotak di sekeliling wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # --- BARU: Logika Deteksi Mata di Dalam Wajah ---
        # 1. Buat Region of Interest (ROI) untuk area wajah
        #    Kita ambil potongan gambar (baik grayscale maupun berwarna) hanya di area kotak wajah
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 2. Deteksi mata HANYA di dalam ROI wajah
        #    Parameter di sini mungkin perlu disesuaikan juga
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(15, 15))

        # 3. Gambar kotak di sekeliling mata yang terdeteksi
        #    Koordinat mata (ex, ey) relatif terhadap ROI, jadi perlu ditambahkan (x, y)
        for (ex, ey, ew, eh) in eyes:
            # Gambar persegi panjang biru di frame asli
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
            # Alternatif jika ingin menggambar di frame utama:
            # cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)
        # --- AKHIR LOGIKA DETEKSI MATA ---

    # Tampilkan frame
    cv2.imshow('Webcam Feed - Deteksi Wajah & Mata', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Webcam ditutup.")