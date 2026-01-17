import qrcode
data = input('Enter the text or URL to encode in QR code: ').strip()
filename = input('Enter the filename to save the QR code image (e.g., qr_code.png): ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f'QR code saved as {filename}')

