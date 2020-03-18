import qrcode
import os
from PIL import Image

def generate_qr(carnet_id):
    qr = qrcode.QRCode(
        version=12,   
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
        )

    qr.add_data(carnet_id)
    qr.make()
    img = qr.make_image()
    
    filename = os.getcwd() + "/engine/database/qrcodes/" + str(carnet_id) + ".png"
    img.save(filename)


def generate_label(first_name, last_name, carnet_id):
    qr = os.getcwd() + "/qrcodes/" + str(carnet_id) + ".png"