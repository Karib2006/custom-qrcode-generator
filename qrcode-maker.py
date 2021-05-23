import pyqrcode
import random
from pyqrcode import QRCode

url = input('Give the link: ')
qr = pyqrcode.create(url)

num = str(random.choice(range(1000)))

file_name = f'Qrcode_{num}.svg'

ss = qr.svg(file_name, scale=8)

print('QR code successfully created !! Note - *Its saved on the file where you saved this program')


