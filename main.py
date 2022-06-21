# imports
import pyqrcode

# main
while True:
    try:
        url = input('Please insert the URL that will be converted into a QR Code (example: https://google.com/): ')
        qrcode = pyqrcode.create(url)
        qrcode.show()
        break
    except Exception as e:
        print(f'\nError: {e}\n')
