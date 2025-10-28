import cv2
import numpy as np
from collections import deque

# Masukkan nilai HSV Anda yang sudah di-tuning
lower_bound = np.array([0, 203, 51])
upper_bound = np.array([179, 255, 204])

paint_canvas = None
points = deque(maxlen=64)

cap = cv2.VideoCapture(0)
if not cap.isOpened(): exit()

print("Mulai menggambar! Gerakkan objek berwarna.")
print("Tekan 'c' untuk membersihkan kanvas. Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)

    if paint_canvas is None: paint_canvas = np.zeros_like(frame)

    # 1. Perhalus gambar
    blurred_frame = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # 2. Buat mask & Perkuat pembersihan
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    # 3. Temukan Pusat Kuas (dengan filter area)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None
    valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

    if len(valid_contours) > 0:
        c = max(valid_contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    points.appendleft(center)

    # Gambar Jejak
    for i in range(1, len(points)):
        if points[i - 1] is None or points[i] is None: continue
        cv2.line(paint_canvas, points[i - 1], points[i], (255, 255, 255), 5)

    # Gabungkan Frame & Kanvas
    frame_masked = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    final_frame = cv2.bitwise_or(frame_masked, paint_canvas)

    cv2.imshow("Air Painter", final_frame)
    # cv2.imshow("Mask", mask) # Aktifkan jika perlu debug hehe

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    elif key == ord('c'):
        paint_canvas = np.zeros_like(frame)
        points.clear()

cap.release()
cv2.destroyAllWindows()