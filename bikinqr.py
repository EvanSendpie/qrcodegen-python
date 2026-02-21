import qrcode

url = input("Masukkan url: ").strip()
file_path = "D:\\outputPy\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code sudah berhasil digenerate")

# Jalankan dengan command di terminal "python .\bikiqr.py"