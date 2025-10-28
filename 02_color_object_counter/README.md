# Proyek 2: Penghitung Objek Berwarna 🎨🔢

Skrip Python ini dirancang untuk mendeteksi dan menghitung jumlah objek dengan warna tertentu dalam sebuah gambar. Fitur utamanya adalah kemampuannya memisahkan objek yang saling bersentuhan menggunakan algoritma Watershed.

Proyek ini juga dilengkapi *tool* terpisah (`hsv_color_picker.py`) untuk membantu mencari rentang warna HSV yang tepat secara interaktif.

## Fitur ✨

* **Deteksi Warna HSV:** Mengisolasi objek berdasarkan rentang warna Hue, Saturation, dan Value.
* **Segmentasi Watershed:** Memisahkan objek-objek yang warnanya sama tapi saling menempel atau tumpang tindih.
* **Pembersihan Mask:** Menggunakan operasi morfologi (Open & Close) untuk mengurangi *noise* dan menyempurnakan *mask* warna.
* **Penghitungan & Visualisasi:** Menghitung jumlah objek yang terdeteksi dan menggambar kotak di sekelilingnya.
* **Pilih File Interaktif:** Menggunakan Tkinter untuk memunculkan dialog pilih file gambar.
* **Pemuatan Gambar Tangguh:** Menggunakan Pillow untuk bisa membuka berbagai format gambar (termasuk WEBP).
* **Window Fleksibel:** Jendela tampilan OpenCV bisa diubah ukurannya.
* **Tool Kalibrasi HSV:** Skrip `hsv_color_picker.py` menyediakan slider *real-time* untuk mencari rentang HSV.

## Teknologi 🚀

* Python
* OpenCV
* NumPy
* Pillow (PIL)
* Tkinter (untuk utilitas `select_image_file`)

## Cara Pakai

1.  **(Kalibrasi Warna - Opsional tapi direkomendasikan)**
    * Jalankan `python hsv_color_picker.py`.
    * Pilih gambar sampel.
    * Geser slider H, S, V sampai objek target berwarna putih di jendela 'Mask'.
    * Klik jendela gambar, tekan 'q'.
    * Salin nilai `lower_bound` dan `upper_bound` dari terminal.
2.  **(Menjalankan Penghitung)**
    * Buka `object_counter.py`.
    * Tempel nilai `lower_bound` dan `upper_bound` yang tadi disalin.
    * Pastikan sudah di *virtual environment* folder ini dan `pip install -r requirements.txt`.
    * Jalankan `python object_counter.py`.
    * Pilih gambar yang ingin dihitung objeknya.
    * Hasilnya akan muncul di jendela baru.