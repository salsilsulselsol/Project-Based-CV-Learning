import cv2
import numpy as np
import sys
from utils import select_image_file, load_image_robustly

# Minta pengguna memilih file
image_path = select_image_file()
if image_path is None:
    sys.exit()

# Gunakan fungsi yang aman untuk memuat gambar
print(f"Mencoba memuat gambar: {image_path}")
image = load_image_robustly(image_path)

if image is None:
    print(f"Error: Gagal memuat gambar dari path: {image_path}")
    sys.exit()

# Konversi ke HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

# Daftarkan semua window yang akan kita gunakan dengan flag WINDOW_NORMAL
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.namedWindow('Trackbars', cv2.WINDOW_AUTOSIZE)

# Atur ukuran awal window agar tidak terlalu besar/kecil
window_width = 500
h, w = image.shape[:2]
aspect_ratio = h / w if w > 0 else 1
cv2.resizeWindow('Original Image', window_width, int(window_width * aspect_ratio))
cv2.resizeWindow('Mask', window_width, int(window_width * aspect_ratio))
cv2.resizeWindow('Result', window_width, int(window_width * aspect_ratio))
cv2.resizeWindow('Trackbars', 640, 240)

# Buat 6 slider untuk rentang HSV
cv2.createTrackbar('H Min', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('H Max', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('S Min', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('S Max', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('V Min', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('V Max', 'Trackbars', 255, 255, nothing)

print("Geser-geser slider sampai warna target Anda menjadi putih di jendela 'Mask'.")
print("Klik salah satu jendela gambar, lalu tekan tombol 'q' untuk keluar.")

while True:
    # Baca posisi slider saat ini
    h_min = cv2.getTrackbarPos('H Min', 'Trackbars')
    h_max = cv2.getTrackbarPos('H Max', 'Trackbars')
    s_min = cv2.getTrackbarPos('S Min', 'Trackbars')
    s_max = cv2.getTrackbarPos('S Max', 'Trackbars')
    v_min = cv2.getTrackbarPos('V Min', 'Trackbars')
    v_max = cv2.getTrackbarPos('V Max', 'Trackbars')

    # Pastikan min <= max
    if h_min > h_max: cv2.setTrackbarPos('H Max', 'Trackbars', h_min)
    if s_min > s_max: cv2.setTrackbarPos('S Max', 'Trackbars', s_min)
    if v_min > v_max: cv2.setTrackbarPos('V Max', 'Trackbars', v_min)

    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])

    # Buat mask dan terapkan ke gambar
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Tampilkan hasilnya secara real-time
    cv2.imshow('Original Image', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Setelah loop berhenti, cetak nilai terakhir yang Anda temukan
print("\nRentang HSV yang Anda temukan:")
print(f"lower_bound = np.array([{h_min}, {s_min}, {v_min}])")
print(f"upper_bound = np.array([{h_max}, {s_max}, {v_max}])")