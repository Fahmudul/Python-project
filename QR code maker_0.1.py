import qrcode as qr
img = qr.make(input("Enter the url you want to make in a qrcode form :\n"))
img.save("google_home_page.png")