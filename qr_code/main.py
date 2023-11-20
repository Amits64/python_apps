import qrcode
from PIL import Image

img = qrcode.make('https://github.com/amits64/prometheus.git')
img.save('myQRcode.png')

img.show()
