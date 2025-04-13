import qrcode

data = input("What should be contents of the qr code?")

qr = qrcode.QRCode()
qr.add_data(data)
qr.make()

qr.print_ascii()  
