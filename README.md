# Simple QR Code Generator

Sebuah script Python sederhana untuk men-generate QR Code dari input URL atau teks dan menyimpannya ke dalam format gambar `.png`.

## Fitur
* Meminta input URL/teks secara interaktif melalui terminal.
* Menggunakan library `qrcode` dan `Pillow` untuk menghasilkan gambar QR Code berkualitas tinggi.
* Proses instalasi yang bersih menggunakan Virtual Environment.

## Prasyarat
Pastikan kamu sudah menginstal **Python 3** di komputermu.

## Cara Instalasi & Setup

1. **Clone repository ini** (atau download file script-nya):
   ```bash
   git clone [https://github.com/EvanSendpie/qrcodegen-python.git](https://github.com/EvanSendpie/qrcodegen-python.git)
   cd qrcodegen-python

2. **Buat Virtual Environment**
   ```bash
   python -m venv .venv

3. **Aktifkan Virtual Environment**
   
   Di Windows:
   ```bash
   .\.venv\Scripts\activate
    ```
   Di Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```
   
4.  **Install Dependencies**
   
   ```bash
   pip install "qrcode[pil]"
   ```

**Cara Penggunaan**
1. Pastikan virtual environment sedang aktif (ada tanda (.venv) di terminal).
2. Jalankan script-nya:
   ```bash
   python bikinqr.py
   ```
3. Masukkan URL atau teks saat diminta
4. Selesai! Script akan memunculkan pesan QR Code sudah berhasil digenerate.
