import qrcode

# Define the website URL
website_url = "https://margaridaealberto.pythonanywhere.com"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(website_url)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_image.save("website_qrcode.png")
