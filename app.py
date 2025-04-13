import qrcode

data = input("Was soll im QR-Code stehen? ")

qr = qrcode.QRCode()
qr.add_data(data)
qr.make()

qr.print_ascii()  # QR-Code wird im Terminal als ASCII ausgegeben
