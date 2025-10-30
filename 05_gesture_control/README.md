# Proyek 5: Kontrol Volume dengan Gestur Tangan 🖐️🔊

Aplikasi ini menggunakan webcam untuk mendeteksi *landmark* tangan secara *real-time* menggunakan MediaPipe. Dengan mengukur jarak antara ujung ibu jari dan jari telunjuk, pengguna bisa mengontrol volume sistem komputer secara langsung.

Proyek ini adalah lompatan dari Computer Vision klasik ke penggunaan model *Deep Learning* modern (MediaPipe) untuk deteksi yang lebih akurat dan interaksi yang canggih.

## Fitur ✨

* **Deteksi Tangan Canggih:** Menggunakan **MediaPipe Hands** dari Google untuk mendapatkan 21 titik *landmark* tangan secara *real-time*.
* **Interpretasi Gestur:** Menghitung jarak antara ujung ibu jari (Landmark #4) dan jari telunjuk (Landmark #8) untuk menentukan level volume.
* **Kontrol Volume Sistem:** Menggunakan *library* **`pycaw`** untuk berinteraksi langsung dengan audio Windows dan mengatur *master volume*.
* **Visualisasi Real-Time:** Menampilkan *feed* webcam dengan *volume bar* virtual dan garis yang menunjukkan gestur jari.
* **Kalibrasi:** Kode ini dirancang agar mudah dikalibrasi (mengubah rentang jarak min/maks) agar sesuai dengan tangan dan preferensi pengguna.

## Teknologi 🚀

* Python (dibuat khusus untuk **v3.12** karena kompatibilitas `mediapipe`)
* OpenCV (untuk akses kamera dan visualisasi)
* MediaPipe (untuk deteksi tangan)
* NumPy (untuk *mapping* nilai `np.interp`)
* pycaw & comtypes (untuk kontrol audio Windows)

## Cara Pakai

**Sangat Penting: Proyek ini butuh Python 3.12 (atau 3.11/3.10).** Library `mediapipe` belum tentu kompatibel dengan versi Python terbaru (seperti 3.13+).

1.  **Buat `venv` dengan Python 3.12:**
    * Pastikan kamu sudah meng-install Python 3.12 di komputermu.
    * Di dalam folder `05_gesture_control` ini, buat `venv` baru:
      ```bash
      py -3.12 -m venv venv
      ```

2.  **Aktifkan `venv`:**
    ```bash
    .\venv\Scripts\activate
    ```

3.  **Install *dependencies*:**
    * Pastikan file `requirements.txt` sudah ada.
    * Jalankan:
      ```bash
      pip install -r requirements.txt
      ```

4.  **Jalankan Aplikasi:**
    ```bash
    python gesture_volume_control.py
    ```

5.  **(Penting) Lakukan Kalibrasi Awal:**
    * Saat program berjalan, lihat terminal. Catat nilai "Jarak:" saat jarimu paling dekat dan paling jauh.
    * Buka `gesture_volume_control.py`.
    * Ubah angka `[28, 230]` di baris `vol_percent = np.interp(distance, [28, 230], [0, 100])` dengan angka yang kamu temukan.
    * Simpan dan jalankan lagi. Sekarang volume seharusnya sudah terkalibrasi.

## Cara Kerja Singkat

1.  **Inisialisasi:** Program memuat model MediaPipe dan terhubung ke kontrol audio sistem (`pycaw`).
2.  **Loop Real-Time:**
    * Menangkap *frame* dari webcam dan membaliknya (mirror).
    * Mengubah *frame* ke format RGB (karena MediaPipe butuh RGB).
    * `hands.process(rgb_frame)` menjalankan model deteksi.
3.  **Jika Tangan Terdeteksi:**
    * Program mengambil koordinat `x, y` dari Landmark #4 (ibu jari) dan #8 (telunjuk).
    * `math.hypot()` menghitung jarak piksel di antara keduanya.
    * `np.interp()` (pemetaan pertama) mengubah jarak piksel itu (misal: 20-200) menjadi persentase (0-100).
    * `np.interp()` (pemetaan kedua) mengubah persentase (0-100) menjadi rentang volume sistem (misal: -65.0 dB s/d 0.0 dB).
    * `volume.SetMasterVolumeLevel(...)` mengirim perintah akhir ke Windows.
4.  **Visualisasi:** Program menggambar lingkaran, garis, dan *volume bar* di *frame* untuk *feedback* visual.