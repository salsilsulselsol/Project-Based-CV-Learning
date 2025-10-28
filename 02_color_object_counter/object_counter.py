import cv2
import numpy as np
import sys
from utils import select_image_file, load_image_robustly

# --- TAHAP 1: SETUP ---
image_path = select_image_file()
if image_path is None: sys.exit()
image = load_image_robustly(image_path)
if image is None:
    print(f"Error: Gagal memuat gambar dari path: {image_path}")
    sys.exit()
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# --- TAHAP 2: DETEKSI WARNA ---
lower_bound = np.array([18, 136, 0])
upper_bound = np.array([35, 255, 255])
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
kernel = np.ones((5,5), np.uint8)
cleaned_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

# --- TAHAP 3: SEGMENTASI DENGAN WATERSHED ---
sure_bg = cv2.dilate(cleaned_mask, kernel, iterations=3)
dist_transform = cv2.distanceTransform(cleaned_mask, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(image, markers)
image[markers == -1] = [0, 0, 255]

# --- TAHAP 4: HITUNG & GAMBAR KOTAK ---
labels = np.unique(markers)
object_count = 0
for label in labels:
    if label < 2:
        continue
    object_mask = np.zeros(markers.shape, dtype="uint8")
    object_mask[markers == label] = 255
    contours, _ = cv2.findContours(object_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(c)
        if area > 500:
            object_count += 1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f"#{object_count}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


# --- TAHAP 5: TAMPILKAN HASIL AKHIR ---
h, w = image.shape[:2]

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text_color = (0, 0, 255)
text_pos_y = 30 

# Jika gambar sangat kecil, kecilkan font dan naikkan posisi teks
if h < 100 or w < 400:
    font_scale = 0.5
    font_thickness = 1
    text_pos_y = 20

# Tulis jumlah total objek yang ditemukan menggunakan variabel dinamis
cv2.putText(image, f"Total Objek Terdeteksi: {object_count}", (10, text_pos_y), font, font_scale, text_color, font_thickness)


# Daftarkan dan atur ukuran window
cv2.namedWindow('Hasil Akhir (Watershed)', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask Awal', cv2.WINDOW_NORMAL)
cv2.namedWindow('Inti Objek (Sure FG)', cv2.WINDOW_NORMAL)
window_width = 600
h_win, w_win = image.shape[:2]
aspect_ratio = h_win / w_win if w_win > 0 else 1
cv2.resizeWindow('Hasil Akhir (Watershed)', window_width, int(window_width * aspect_ratio))
cv2.resizeWindow('Mask Awal', window_width, int(window_width * aspect_ratio))
cv2.resizeWindow('Inti Objek (Sure FG)', window_width, int(window_width * aspect_ratio))

# Tampilkan semua jendela
cv2.imshow('Hasil Akhir (Watershed)', image)
cv2.imshow('Mask Awal', cleaned_mask)
cv2.imshow('Inti Objek (Sure FG)', sure_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()