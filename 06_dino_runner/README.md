# Proyek 6: Kontrol Game Dino dengan Gestur 🦖🖐️

Aplikasi ini memungkinkan kamu bermain game Dinosaurus Chrome (`chrome://dino`) tanpa menyentuh keyboard. Cukup angkat jari telunjukmu di depan webcam untuk membuat si Dinosaurus melompat.

Proyek ini adalah langkah selanjutnya dari deteksi landmark, di mana kita beralih dari *membaca* data (seperti jarak) menjadi *mengklasifikasikan* sebuah pose (jari ke atas vs. jari ke bawah) untuk memicu aksi diskrit (menekan tombol).

## Fitur ✨

* **Klasifikasi Gestur Sederhana:** Menggunakan landmark dari MediaPipe untuk mendeteksi pose "jari telunjuk menunjuk ke atas".
* **Kontrol Keyboard:** Menggunakan `pynput` untuk mengirim perintah "Spasi" ke komputer dengan latensi rendah.
* **Manajemen Status (Cooldown):** Mengimplementasikan logika *cooldown* untuk mencegah lompatan beruntun yang tidak disengaja, membuat kontrol lebih stabil.
* **Deteksi Tangan Real-Time:** Menggunakan MediaPipe Hands untuk deteksi landmark tangan yang akurat dan cepat.

## Teknologi 🚀

* Python (dibuat khusus untuk **v3.12** karena kompatibilitas `mediapipe`)
* OpenCV (untuk akses kamera dan visualisasi)
* MediaPipe (untuk deteksi tangan)
* Pynput (untuk kontrol keyboard)
* `time` (untuk logika *cooldown*)

## Cara Pakai

**PENTING:** Proyek ini membutuhkan **Python 3.12** (atau 3.11/3.10) agar `mediapipe` bisa di-install.

1.  **Buat `venv` dengan Python 3.12:**
    * Pastikan kamu sudah meng-install Python 3.12 di komputermu.
    * Di dalam folder `06_dino_runner` ini, buat `venv`:
      ```bash
      py -3.12 -m venv venv
      ```
    * Aktifkan `venv`:
      ```bash
      .\venv\Scripts\activate
      ```

2.  **Install *dependencies*:**
    * Pastikan file `requirements.txt` sudah ada.
    * Jalankan:
      ```bash
      pip install -r requirements.txt
      ```
    *(Jika belum punya `requirements.txt`, jalankan `pip install opencv-python mediapipe pynput` lalu `pip freeze > requirements.txt`)*

3.  **Jalankan Aplikasi:**
    ```bash
    python dino_runner.py
    ```

4.  **Cara Bermain:**
    * Buka browser Chrome dan ketik `chrome://dino` di *address bar*.
    * Posisikan jendela game dan jendela webcam agar terlihat.
    * **KLIK DI DALAM JENDELA GAME** untuk memberinya "fokus".
    * Angkat jari telunjukmu 👆 untuk melompat!
    * Tekan 'q' di jendela webcam untuk keluar.

## Cara Kerja Singkat (Logika Kode)

1.  **Inisialisasi:** Program memuat model MediaPipe dan *controller* keyboard `pynput`.
2.  **Loop Real-Time:** Program terus-menerus membaca *frame* dari webcam.
3.  **Deteksi Gestur:**
    * Untuk setiap *frame*, program mendeteksi 21 *landmark* tangan.
    * Ia membandingkan koordinat Y dari **ujung telunjuk (#8)** dengan **sendi tengah telunjuk (#6)**.
    * Jika `Y_ujung < Y_sendi`, gestur dianggap `LOMPAT`.
4.  **Logika Aksi (Tap + Cooldown):**
    * Jika gestur `LOMPAT` terdeteksi **DAN** program sedang dalam status `can_jump` (boleh lompat):
        * Program langsung menjalankan `keyboard.press(Key.space)` dan `keyboard.release(Key.space)` di *frame* yang sama. Ini adalah "tap" instan.
        * Program menyetel `can_jump = False` dan memulai timer *cooldown*.
    * Jika gestur `DIAM`, program akan menunggu *cooldown* selesai (misal 0.4 detik) sebelum menyetel `can_jump = True` lagi.
    * Logika ini memastikan satu gestur hanya menghasilkan satu lompatan, tidak peduli berapa lama jari ditahan di atas.

## Keterbatasan

* **Satu Aksi:** Versi ini hanya melakukan "tap" instan. Kami menemukan bahwa *loop* program (sekitar 30 FPS) terlalu lambat untuk bisa membedakan antara "tap" (1-2 ms) dan "long tap" (33+ ms) yang dibutuhkan game Dino. Oleh karena itu, semua lompatan akan memiliki ketinggian yang sama (lompat tinggi), tapi setidaknya konsisten.