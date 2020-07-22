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

        if greyval > 127:
            bwval = 255
        else:
            bwval = 0
            
        newpixel = image.Pixel(bwval, bwval, bwval)
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()


