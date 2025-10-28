# Belajar Computer Vision (Project-Based Learning) 🚀

Repositori ini adalah catatan perjalanan belajar saya di dunia Computer Vision (CV) melalui pendekatan *project-based learning*. Setiap folder berisi satu proyek spesifik yang fokus pada teknik atau konsep CV tertentu, menggunakan Python dan OpenCV.

---

## Daftar Proyek

Berikut adalah proyek-proyek yang sudah dikerjakan:

1.  **[01_scanner_dokumen_gui](./01_scanner_dokumen_gui/README.md)**
    * **Topik:** Koreksi perspektif, deteksi tepi (Canny), deteksi garis (Hough), normalisasi pencahayaan, GUI (Tkinter), penyesuaian manual.
    * **Deskripsi:** Aplikasi desktop untuk meluruskan foto dokumen yang miring, dilengkapi fitur *tuning* parameter dan *crop* manual.
    * **Status README:** *(Perlu diisi)*

2.  **[02_penghitung_warna](./02_penghitung_warna/README.md)**
    * **Topik:** *Color space* HSV, *masking* warna, operasi morfologi, segmentasi Watershed, analisis kontur.
    * **Deskripsi:** Skrip untuk menghitung objek berdasarkan warna, mampu memisahkan objek yang bersentuhan. Dilengkapi *tool* kalibrasi warna.
    * **Status README:** *(Perlu diisi)*

3.  **[03_detektor_wajah](./03_detektor_wajah/README.md)**
    * **Topik:** Akses webcam *real-time*, Haar Cascades, *Region of Interest* (ROI).
    * **Deskripsi:** Aplikasi *real-time* sederhana untuk mendeteksi wajah dan mata dari webcam.
    * **Status README:** *(Perlu diisi)*

4.  **[04_air_painter](./04_air_painter/README.md)**
    * **Topik:** Pelacakan objek berwarna *real-time*, analisis kontur & momen (centroid), `deque` untuk jejak.
    * **Deskripsi:** Aplikasi untuk "menggambar" di layar dengan menggerakkan objek berwarna di depan webcam. Dilengkapi *tool* kalibrasi warna.
    * **Status README:** *(Perlu diisi)*

*(Catatan: Pastikan nama folder di atas sudah sesuai dengan nama folder kamu yang sebenarnya)*

---

## Setup Umum

Setiap proyek di repositori ini dirancang agar independen. Cara umum untuk menjalankan salah satu proyek:

1.  Masuk ke direktori proyek: `cd NAMA_FOLDER_PROYEK` (contoh: `cd 01_scanner_dokumen_gui`).
2.  Buat *virtual environment*: `python -m venv venv`.
3.  Aktifkan *virtual environment*: `.\venv\Scripts\activate` (Windows) atau `source venv/bin/activate` (Mac/Linux).
4.  Install *dependencies*: `pip install -r requirements.txt`.
5.  Jalankan file Python utamanya (biasanya `app.py` atau nama file utama lainnya).

---
*Repositori ini akan terus bertambah seiring saya melanjutkan perjalanan belajar Computer Vision.*