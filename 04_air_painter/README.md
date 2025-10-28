# Proyek 4: Air Painter ✍️💨

Aplikasi seru ini memungkinkan kamu "melukis" di layar hanya dengan menggerakkan objek berwarna di depan webcam! Program akan melacak objek tersebut dan meninggalkan jejak digital di layar.

Proyek ini fokus pada pelacakan objek berdasarkan warna secara *real-time* dan menggabungkan *feed* video dengan kanvas digital.

## Fitur ✨

* **Pelacakan Warna Real-Time:** Menggunakan rentang warna HSV untuk mendeteksi posisi "kuas" virtual.
* **Menggambar Jejak:** Menyimpan beberapa posisi terakhir kuas (`deque`) dan menggambar garis di antara titik-titik tersebut.
* **Lebih Stabil:** Menggunakan *Gaussian Blur*, operasi morfologi (Open & Close) yang diperkuat, dan filter area kontur untuk mengurangi sensitivitas terhadap *noise* dan perubahan cahaya.
* **Kanvas Digital:** Menampilkan jejak lukisan di atas *feed* video webcam.
* **Kontrol:** Tekan 'c' untuk membersihkan kanvas, 'q' untuk keluar.
* **Tool Kalibrasi HSV:** Skrip terpisah (`air_painter_check.py`) untuk mencari rentang warna HSV kuas secara interaktif.

## Teknologi 🚀

* Python
* OpenCV
* NumPy
* `collections.deque`

## Cara Pakai

1.  **(Kalibrasi Warna)**
    * Siapkan objek berwarna cerah (misal: tutup spidol).
    * Jalankan `python air_painter_check.py`.
    * Pilih gambar sampel (bisa *screenshot* dari webcam).
    * Arahkan objek ke kamera. Atur slider H, S, V sampai hanya objekmu yang putih terang di 'Mask'.
    * Klik jendela gambar, tekan 'q'.
    * Salin nilai `lower_bound` dan `upper_bound` dari terminal.
2.  **(Menggambar)**
    * Buka `air_painter.py`.
    * Tempel nilai `lower_bound` dan `upper_bound` yang tadi disalin.
    * Pastikan sudah di *virtual environment* folder ini dan `pip install -r requirements.txt`.
    * Jalankan `python air_painter.py`.
    * Gerakkan objek berwarna di depan kamera untuk mulai melukis!
    * Tekan 'c' untuk hapus, 'q' untuk keluar.