import qrcode
import image
qr = qrcode.QRCode(
    version=4,
    box_size=10,
    border=4,
)
qr.add_data('http://www.unipune.ac.in/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")
