import qrcode
img = qrcode.make("https://www.linkedin.com/in/tithi-d-08220a14b/")

type(img) # qrcode.image.pil.PilImage
img.save("myprofile.jpg")