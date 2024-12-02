import qrcode as qr
img=qr.make("https://www.facebook.com/officialroutineofnepalbanda")
img.save("fbqrcode.png")