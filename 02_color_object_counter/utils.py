import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image

def select_image_file():
    """Memunculkan dialog untuk memilih file gambar."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Pilih sebuah file gambar",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp")]
    )
    if not file_path:
        print("Tidak ada file yang dipilih. Program berhenti.")
        return None
    return file_path

def load_image_robustly(path):
    """
    Membaca gambar dengan cara paling tangguh menggunakan Pillow,
    lalu mengkonversinya ke format OpenCV.
    """
    try:
        # 1. Buka dengan Pillow (bisa membaca banyak format, termasuk WEBP)
        pil_image = Image.open(path)
        
        # 2. Konversi ke format RGB
        pil_image = pil_image.convert('RGB')
        
        # 3. Ubah dari format Pillow ke format OpenCV (NumPy array)
        cv_image = np.array(pil_image)
        
        # 4. Konversi dari RGB (standar Pillow) ke BGR (standar OpenCV)
        cv_image = cv_image[:, :, ::-1].copy()
        
        return cv_image
    except Exception as e:
        print(f"Error fatal saat memuat gambar dengan Pillow: {e}")
        return None