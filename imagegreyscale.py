import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,120)   # setDelay(0) turns off animation
#img.setDelay(0)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = p.getRed()
        newgreen = p.getGreen()
        newblue = p.getBlue()
        
        greyval = (newred + newgreen + newblue)/3

        newpixel = image.Pixel(greyval, greyval, greyval)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()

