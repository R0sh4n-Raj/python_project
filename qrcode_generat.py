# How to generatwe a QR code in Python?

# import qrcode as qr
# img = qr.make("(R4j$&6@)")

# img.save("Wifi_pwd.png")



import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://thinksys.com/services/software-development/')
qr.make(fit=True)
img = qr.make_image(fill_color="gray", back_color="white")
img.save("roshan_linkedin.png")