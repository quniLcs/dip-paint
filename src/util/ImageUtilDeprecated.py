# coding = utf-8

from PyQt5.QtGui import QImage,qRed,qGreen,qBlue,qRgba,qAlpha,QColor


def bound(low,high,value):
    return low if value < low else high if value > high else value


# 调整亮度
def adjustBright(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    for w in range(width):
        for h in range(height):
            pixel = QColor(image.pixel(w, h))
            red = (pixel.red() + value)
            red = bound(0,255,red)
            green = (pixel.green() + value)
            green = bound(0, 255, green)
            blue = (pixel.blue() + value)
            blue = bound(0,255,blue)
            # if red != 205:
            #     pass
            newImage.setPixel(w, h, qRgba(red, green, blue, pixel.alpha()))
    return newImage


# 调整暖色调
def adjustWarm(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    for w in range(width):
        for h in range(height):
            pixel = QColor(image.pixel(w, h))
            red, green, blue = pixel.red(), pixel.green(), pixel.blue()
            if value >= 0:
                red += value
                red = bound(0,255,red)
                green += value
                green = bound(0,255,green)
            else:
                blue += abs(value)
                blue = bound(0,255,blue)
            newImage.setPixel(w, h, qRgba(red, green, blue, pixel.alpha()))
    return newImage


# 调整饱和度
def adjustSaturation(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    for w in range(width):
        for h in range(height):
            pixel = QColor(image.pixel(w, h)).toHsl()
            H = pixel.hue()
            S = pixel.saturation() + value
            L = pixel.lightness()
            S = bound(0,255,S)
            pixel.setHsl(H, S, L);
            newImage.setPixel(w, h, qRgba(pixel.red(), pixel.green(), pixel.blue(), pixel.alpha()))
    return newImage


# 调整对比度
def adjustContrast(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    if value >= 0:
        value = 1 / (1 - value / 100.0) - 1
    else:
        value /= 100.0
    for w in range(width):
        for h in range(height):
            pixel = QColor(image.pixel(w, h))
            color = [bound(0,255,(c - 127) * value + c) for c in [pixel.red(), pixel.green(), pixel.blue()]]
            newImage.setPixel(w, h, qRgba(*color, pixel.alpha()))
    return newImage
