from ulab import numpy as np
import bitmaptools
from displayio import Bitmap
from ulab import numpy as np

MAX_RADIUS = 100
MIN_RADIUS = 10

def bitmap_to_numpy(bitmap):
    """Converts a displayio.Bitmap into a numpy array that's viewable by OpenCV"""
    # Create a numpy array, 3 bytes for each pixel
    height = bitmap.height
    width = bitmap.width
    r_channel = np.zeros((height, width), dtype=np.uint8)
    g_channel = np.zeros((height, width), dtype=np.uint8)
    b_channel = np.zeros((height, width), dtype=np.uint8)
    # Iterate through each pixel
    for x in range(bitmap.width):
        for y in range(bitmap.height):
            pixel = bitmap[x, y]
            # rgb565 to rgb888
            r = (pixel & 0xF800) >> 8
            g = (pixel & 0x07E0) >> 3
            b = (pixel & 0x001F) << 3
            # Store in numpy array
            r_channel[y, x] = r
            g_channel[y, x] = g
            b_channel[y, x] = b
    return r_channel, g_channel, b_channel

def histogram(data, bins):
    hist = np.zeros(len(bins)-1, dtype=np.int16)
    for d in data:
        for i in range(len(bins)-1):
            if bins[i] <= d < bins[i+1]:
                hist[i] += 1
                break
    return hist

def convolve2d(img, kernel):
    output = np.zeros((img.shape[0] - kernel.shape[0] + 1, img.shape[1] - kernel.shape[1] + 1))
    for x in range(output.shape[0]):
        for y in range(output.shape[1]):
            output[x,y] = np.sum(img[x:x+kernel.shape[0], y:y+kernel.shape[1]] * kernel)
    return output

def rgb_to_gray(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b


def apply_sobel(img):
    sobel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    gx = convolve2d(img, sobel_x)
    gy = convolve2d(img, sobel_y)

    mag = np.sqrt(gx**2 + gy**2)

    return mag

def detect_concentric_circles(bitmap565):
    r_channel, g_channel, b_channel = bitmap_to_numpy(bitmap565)

    # Convert to grayscale
    gray = rgb_to_gray(r_channel, g_channel, b_channel)

    edges = apply_sobel(gray)
    
    condition = (edges > 0)
    x_indices = np.where(condition, np.arange(edges.shape[0]), 0).flatten()
    y_indices = np.where(condition, np.arange(edges.shape[1]), 0).flatten()
    x_indices = x_indices[x_indices != 0]
    y_indices = y_indices[y_indices != 0]

    center = (int(np.mean(x_indices)), int(np.mean(y_indices)))

    distance = np.sqrt((x_indices - center[0])**2 + (y_indices - center[1])**2)
    hist = histogram(distance, bins=range(0, MAX_RADIUS+2))

    radii = []

    for r in range(MIN_RADIUS, MAX_RADIUS):
        if hist[r] > hist[r-1] and hist[r] > hist[r+1]:
            radii.append(r)

    return center, radii


bp = Bitmap(160,160, 0xffff)
fp = open('target.png')

bitmaptools.lodepng(bp,fp)

c, r = detect_concentric_circles(bp)

print(c, r)

