from ulab import numpy as np
import bitmaptools
from displayio import Bitmap
from ulab import numpy as np

def rgb_to_gray(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b

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
    gray = rgb_to_gray(r_channel, g_channel, b_channel)
    return gray

def frame_diff(img1, img2):
    diff = abs(img1 - img2)
    return diff

def binarize(img, threshold):
    return np.where(img > threshold, 255, 0)

def find_ball_position(diff_img):
    y_indices, x_indices = np.nonzero(diff_img)

    if len(x_indices) == 0:
        return None
    ball_center = (int(np.mean(x_indices)), int(np.mean(y_indices)))
    return ball_center


bp = Bitmap(160,160, 0xffff)
fp = open('target.png')
bitmaptools.lodepng(bp,fp)

bp2 = Bitmap(160,160, 0xffff)
fp2 = open('target1.png')
bitmaptools.lodepng(bp2,fp2)

diff_img = frame_diff(bitmap_to_numpy(bp), bitmap_to_numpy(bp2))

bin_img = binarize(diff_img, 50)

ball_center = find_ball_position(bin_img)

print(ball_center)