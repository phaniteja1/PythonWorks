__author__ = 'phaniteja'

# This program is to get the required pixel values from a file, store them and perform transformations

# Import the modules to perform operations on Image - PIL is used for operations
from PIL import Image


image = Image.open("steve.jpg")

image = image.convert('RGB')        # Convert the image to RGB type

width, height = image.size

all_pixels = []                     # Array to store the pixel values

# pix = getPixel(image,1,1)
