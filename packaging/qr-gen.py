# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
# String which represents the QR code 
s = "orangecrab.gregdavill.com"

# Generate QR code 
url = pyqrcode.create(s, error='L') 

# Create and save the svg file
url.svg("orangecrab_qr.svg", scale = 8)
