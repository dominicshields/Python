import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,120)   # setDelay(0) turns off animation
#img.setDelay(0)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        
        newred = (red * 0.393 + green * 0.769 + blue * 0.189)
        newgreen = (red * 0.349 + green * 0.686 + blue * 0.168)
        newblue = (red * 0.272 + green * 0.534 + blue * 0.131)
           
        newpixel = image.Pixel(newred, newgreen, newblue)
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()



