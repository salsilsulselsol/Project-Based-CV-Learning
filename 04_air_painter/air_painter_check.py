import cv2
import numpy as np

# Fungsi dummy untuk trackbar
def nothing(x):
    pass

# Akses webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

# Buat window untuk trackbar
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)

# Buat trackbar untuk H, S, V
cv2.createTrackbar("H Min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H Max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("S Min", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("S Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V Min", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("V Max", "Trackbars", 255, 255, nothing)

print("Arahkan objek berwarna ke kamera.")
print("Atur slider hingga objek Anda berwarna putih terang di jendela 'Mask'.")
print("Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal membaca frame.")
        break

    # Balik frame secara horizontal (mirror) agar gerakan terasa natural
    frame = cv2.flip(frame, 1)

    # Konversi ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Baca nilai dari trackbar
    h_min = cv2.getTrackbarPos("H Min", "Trackbars")
    h_max = cv2.getTrackbarPos("H Max", "Trackbars")
    s_min = cv2.getTrackbarPos("S Min", "Trackbars")
    s_max = cv2.getTrackbarPos("S Max", "Trackbars")
    v_min = cv2.getTrackbarPos("V Min", "Trackbars")
    v_max = cv2.getTrackbarPos("V Max", "Trackbars")

    # Buat mask
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bersihkan mask sedikit
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Tampilkan frame asli dan mask
    cv2.imshow("Webcam Feed", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nNilai HSV terakhir:")
print(f"lower_bound = np.array([{h_min}, {s_min}, {v_min}])")
print(f"upper_bound = np.array([{h_max}, {s_max}, {v_max}])")
print("Gunakan nilai ini di air_painter.py")