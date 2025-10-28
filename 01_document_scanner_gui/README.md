# Proyek 1: Scanner Dokumen GUI 📄

Aplikasi desktop ini berfungsi seperti scanner dokumen portabel. Kamu bisa pilih foto dokumen yang diambil miring, lalu aplikasi ini akan mencoba meluruskannya secara otomatis. Kalau deteksi otomatisnya kurang pas, ada fitur buat *crop* manual pakai mouse.

Ini adalah versi pengembangan dari skrip *command-line* sederhana, dilengkapi dengan GUI yang lebih ramah pengguna dan algoritma yang lebih canggih.

## Fitur ✨

* **GUI Interaktif:** Dibangun pakai Tkinter, lengkap dengan preview gambar asli dan hasil scan.
* **Deteksi Otomatis:** Mencoba menemukan 4 sudut dokumen pakai kombinasi Canny, Dilasi, dan Hough Transform.
* **Penghilang Bayangan:** Ada langkah pra-pemrosesan untuk mengurangi efek bayangan pada dokumen.
* **Penyesuaian Manual:** Jendela *pop-up* muncul setelah deteksi otomatis, memungkinkan kamu menggeser 4 titik sudut area *scan* secara presisi.
* **Tuning Parameter:** Slider untuk mengatur parameter Canny dan Hough biar deteksi otomatisnya bisa disesuaikan.
* **Filter B&W:** Opsi untuk mengubah hasil scan jadi hitam-putih.
* **Simpan Hasil:** Hasil scan bisa disimpan sebagai file JPG/PNG.

## Teknologi 🚀

* Python
* OpenCV
* NumPy
* Pillow (PIL)
* Tkinter

## Cara Pakai

1.  Pastikan sudah di *virtual environment* folder ini dan `pip install -r requirements.txt`.
2.  Jalankan `python app.py`.
3.  Klik "Pilih Gambar" untuk memilih foto dokumen.
4.  Klik "Deteksi & Sesuaikan".
5.  Atur 4 titik merah di jendela *pop-up* jika perlu, lalu klik "Terapkan".
6.  Gunakan *checkbox* B&W jika mau.
7.  Klik "Simpan Gambar".