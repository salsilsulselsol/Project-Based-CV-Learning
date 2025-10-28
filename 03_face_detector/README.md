# Proyek 3: Detektor Wajah & Mata Real-Time 😃👁️

Aplikasi sederhana ini menggunakan webcam untuk mendeteksi wajah dan mata secara *real-time*. Deteksi dilakukan menggunakan metode klasik Haar Cascades yang disediakan oleh OpenCV.

Ini adalah proyek pengantar yang bagus untuk pemrosesan video *live* dan penggunaan *classifier* siap pakai.

## Fitur ✨

* **Akses Webcam:** Menangkap *feed* video langsung dari kamera default.
* **Deteksi Wajah:** Menggunakan `haarcascade_frontalface_default.xml` untuk menemukan wajah dalam *frame*.
* **Deteksi Mata:** Menggunakan `haarcascade_eye.xml` untuk menemukan mata **di dalam** area wajah yang sudah terdeteksi (*Region of Interest*).
* **Visualisasi Real-Time:** Menggambar kotak hijau di sekitar wajah dan kotak biru di sekitar mata.

## Teknologi 🚀

* Python
* OpenCV
* NumPy (digunakan secara implisit oleh OpenCV)

## Cara Pakai

1.  Pastikan sudah di *virtual environment* folder ini dan `pip install -r requirements.txt`.
2.  Pastikan file `haarcascade_frontalface_default.xml` dan `haarcascade_eye.xml` ada di folder yang sama.
3.  Jalankan `python face_detector.py`.
4.  Hadapkan wajah ke kamera. Kotak deteksi akan muncul.
5.  Tekan 'q' untuk keluar.

## Cara Kerja Singkat (Haar Cascades)

Metode ini tidak pakai *deep learning*. Ia bekerja cepat dengan:
1.  Menggunakan **fitur Haar** (pola kotak hitam-putih sederhana) untuk mencari kontras gelap-terang (misal: area mata lebih gelap dari dahi).
2.  Menggunakan **gambar integral** untuk menghitung fitur dengan sangat cepat.
3.  Menggunakan **kaskade** (pos pemeriksaan bertingkat). Area gambar akan langsung dibuang jika gagal melewati tes fitur sederhana di tahap awal, jadi tidak perlu dites dengan semua fitur. Hanya area yang lolos semua tahap yang dianggap sebagai wajah/mata.