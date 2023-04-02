import numpy
import math
from PIL import Image
import pygame


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

def convert_to_grayscale(image_obj):
    grayscale_image = []
    for pixel in image_obj:
        for y in pixel:
            gray_value = int(y[0] + y[1] + y[2]) / 3
            grayscale_image.append(gray_value)
    
    return grayscale_image

# variables
image = get_image("D:\Programs\ASCII CONVERTER\paint.jpg")
image_rows = len(image)
image_col = len(image[0])

gray_img_vals = convert_to_grayscale(image)
ascii_chars = 'Ñ@#W$9876543210?!abc;:+=-,._ '
len_ascii = len(ascii_chars)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

for i in range(image_rows):
    for j in range(image_col):
        char_ind = math.floor(translate(gray_img_vals[j] , 0, 255, len_ascii-1, 0))
        print(ascii_chars[char_ind], end='')
    print()
     


# TODO make it work 