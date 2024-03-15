# coding = utf-8

from PyQt5.QtGui import QImage
import cv2 as cv
import numpy as np
# import copy


def crop(image, x1, y1, x2, y2):
    src = QImageToCvMat(image)
    dst = np.ones((y2 - y1, x2 - x1, 4), np.uint8) * 255

    width = image.width()
    height = image.height()

    if x1 < 0:
        x1_src = 0
        x1_dst = -x1
    else:
        x1_src = x1
        x1_dst = 0

    if y1 < 0:
        y1_src = 0
        y1_dst = -y1
    else:
        y1_src = y1
        y1_dst = 0

    if x2 > width:
        x2_src = width
        x2_dst = width - x1
    else:
        x2_src = x2
        x2_dst = x2 - x1

    if y2 > height:
        y2_src = height
        y2_dst = height - y1
    else:
        y2_src = y2
        y2_dst = y2 - y1

    dst[y1_dst: y2_dst, x1_dst: x2_dst] = src[y1_src: y2_src, x1_src: x2_src]
    return CvMatToQImage(dst)


def drawBucket(image, pos, fillColor):
    x = pos.x()
    y = pos.y()

    src = QImageToCvMat(image)
    targetColor = src[y, x]
    targetColorMask = (
            (src[:, :, 0] == targetColor[0]) &
            (src[:, :, 1] == targetColor[1]) &
            (src[:, :, 2] == targetColor[2]) &
            (src[:, :, 3] == targetColor[3])
    )

    kernel = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])
    fillMask = np.zeros_like(targetColorMask)
    current = np.zeros_like(targetColorMask)
    current[y, x] = 1

    while current.any():
        fillMask |= current
        current = current.astype(np.uint8)
        current = cv.filter2D(current, -1, kernel)
        current = current.astype(np.bool)
        current &= targetColorMask
        current &= ~fillMask

    dst = src.copy()
    dst[fillMask] = np.array([fillColor.red(), fillColor.green(), fillColor.blue(), fillColor.alpha()])
    return CvMatToQImage(dst)


def adjustBrightFaster(image: QImage, value) -> QImage:
    src = QImageToCvMat(image)
    src = src.astype(np.int16)

    dst = np.zeros_like(src)
    dst[:, :, 0:3] = src[:, :, 0:3] + value
    dst[:, :, 3] = src[:, :, 3]

    dst[dst < 0] = 0
    dst[dst > 255] = 255

    dst = dst.astype(np.uint8)
    return CvMatToQImage(dst)


def adjustWarmFaster(image: QImage, value) -> QImage:
    src = QImageToCvMat(image)
    src = src.astype(np.int16)

    dst = np.zeros_like(src)
    if value >= 0:
        dst[:, :, 0:2] = src[:, :, 0:2] + value
        dst[:, :, 2:4] = src[:, :, 2:4]
    else:
        dst[:, :, 0:2] = src[:, :, 0:2]
        dst[:, :, 2] = src[:, :, 2] + abs(value)
        dst[:, :, 3] = src[:, :, 3]

    dst[dst < 0] = 0
    dst[dst > 255] = 255

    dst = dst.astype(np.uint8)
    return CvMatToQImage(dst)


def adjustSaturationFaster(image: QImage, value) -> QImage:
    src = QImageToCvMat(image)
    hls = cv.cvtColor(src, cv.COLOR_RGB2HLS)
    hls = hls.astype(np.int16)

    dst = np.zeros_like(hls)
    dst[:, :, 0:2] = hls[:, :, 0:2]
    dst[:, :, 2] = hls[:, :, 2] + value

    dst[dst < 0] = 0
    dst[dst > 255] = 255

    dst = dst.astype(np.uint8)
    dst = cv.cvtColor(dst, cv.COLOR_HLS2RGB)
    dst = cv.cvtColor(dst, cv.COLOR_RGB2RGBA)
    return CvMatToQImage(dst)


def adjustContrastFaster(image: QImage, value) -> QImage:
    value /= 100.0
    if value >= 0:
        value = 1 / (1 - value) - 1

    src = QImageToCvMat(image)
    src = src.astype(np.float32)

    dst = np.zeros_like(src)
    dst[:, :, 0:3] = (src[:, :, 0:3] - 127) * value + src[:, :, 0:3]
    dst[:, :, 3] = src[:, :, 3]

    dst[dst < 0] = 0
    dst[dst > 255] = 255

    dst = dst.astype(np.uint8)
    return CvMatToQImage(dst)


def QImageToCvMat(incomingImage):
    incomingImage = incomingImage.convertToFormat(QImage.Format_RGBA8888)
    width = incomingImage.width()
    height = incomingImage.height()
    ptr = incomingImage.bits()
    ptr.setsize(height * width * 4)
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return arr.copy()


def CvMatToQImage(cvMat):
    if len(cvMat.shape) == 2:
        # 灰度图是单通道，所以需要用Format_Indexed8
        rows, columns = cvMat.shape
        bytesPerLine = columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
    else:
        rows, columns, channels = cvMat.shape
        bytesPerLine = channels * columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_RGBA8888)


def blur(image: QImage):
    src = QImageToCvMat(image)
    blurImg = cv.GaussianBlur(src, (0, 0), sigmaX=15)
    return CvMatToQImage(blurImg)


def sharpen(image: QImage):
    src = QImageToCvMat(image)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    dst = cv.filter2D(src, -1, kernel)

    # blurImg = cv.GaussianBlur(src, (0, 0), 5)
    # usm = cv.addWeighted(src, 1.5, blurImg, -0.5, 0)
    return CvMatToQImage(dst)


def canny(image: QImage):
    src = QImageToCvMat(image)
    blurred = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150)
    return CvMatToQImage(edges)


def gray(image: QImage):
    src = QImageToCvMat(image)
    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    return CvMatToQImage(gray)


def binaryzation(image: QImage):
    src = QImageToCvMat(image)
    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    ret,thresh1 = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    return CvMatToQImage(thresh1)


def invert(image: QImage):
    src = QImageToCvMat(image)
    # res = cv.bitwise_not(src)
    # res = src.copy()
    if len(src.shape) == 2:
        res = 255 - src
        # rows, columns = src.shape
        # for row in range(rows):
        #     for col in range(columns):
        #         res[row, col] = (255 - src[row, col])
    else:
        res = np.zeros_like(src)
        res[:, :, 0:3] = 255 - src[:, :, 0:3]
        res[:, :, 3] = src[:, :, 3]
        # rows, columns, channels = src.shape
        # for row in range(rows):
        #     for col in range(columns):
        #         res[row, col] = (255 - src[row, col][0], 255 - src[row, col][1], 255 - src[row, col][2], src[row, col][3])
    return CvMatToQImage(res)


def emboss(image: QImage):
    src = QImageToCvMat(image)
    kernel = np.array([[-2, -1, 0],
                       [-1, 1, 1],
                       [0, 1, 2]])
    dst = cv.filter2D(src, -1, kernel)
    return CvMatToQImage(dst)


if __name__ == '__main__':
    src = np.ones((413, 658, 4), np.uint8) * 255
    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    pass
