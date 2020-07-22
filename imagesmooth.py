import image
import sys

def double(oldimage):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()

    newim = image.EmptyImage(oldw * 2, oldh * 2)
    for row in range(oldh):
        for col in range(oldw):
            avediv = 0
            red = 0
            green = 0
            blue = 0
            oldpixel = oldimage.getPixel(col, row)
            if col > 1:
                pixel = oldimage.getPixel(col-1, row)
                avediv += 1
                red += pixel.getRed()
                green += pixel.getGreen()
                blue += pixel.getBlue()                
            if col < oldw-1:
                pixel = oldimage.getPixel(col+1, row)
                avediv += 1
                red += pixel.getRed()
                green += pixel.getGreen()
                blue += pixel.getBlue()   
            if row > 1:
                pixel = oldimage.getPixel(col, row-1)
                avediv += 1
                red += pixel.getRed()
                green += pixel.getGreen()
                blue += pixel.getBlue()                
            if row < oldh-1:
                pixel = oldimage.getPixel(col, row+1)
                avediv += 1
                red += pixel.getRed()
                green += pixel.getGreen()
                blue += pixel.getBlue()              
                
            if avediv > 0:
                red = red/avediv
                green = green/avediv
                blue = blue/avediv
                newpixel = image.Pixel(red, green, blue)
                newim.setPixel(2*col, 2*row, newpixel)
                newim.setPixel(2*col+1, 2*row, newpixel)
                newim.setPixel(2*col, 2*row+1, newpixel)
                newim.setPixel(2*col+1, 2*row+1, newpixel)
            else:
                newim.setPixel(2*col, 2*row, oldpixel)
                newim.setPixel(2*col+1, 2*row, oldpixel)
                newim.setPixel(2*col, 2*row+1, oldpixel)
                newim.setPixel(2*col+1, 2*row+1, oldpixel)

    return newim
sys.setExecutionLimit(60000)
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)
img.setDelay(0)
bigimg = double(img)
bigimg.draw(win)

