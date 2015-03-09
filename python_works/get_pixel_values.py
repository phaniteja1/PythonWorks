__author__ = 'phaniteja'

# This program is to get the required pixel values from a file, store them and perform transformations

# Import the modules to perform operations on Image - PIL is used for operations
from PIL import Image


image = Image.open("steve.jpg")

image = image.convert('RGB')        # Convert the image to RGB type

width, height = image.size

all_pixels = []                     # Array to store the pixel values

for x in range(width):
    for y in range(height):
        cpixel = image.getpixel((x, y))          # r, g, b = image.getpixel((x, y))  --> Get the pixel values

        all_pixels.append(cpixel)


# print(all_pixels)

# code to write the pixel values to a file

f = open("pixel_values.csv", "w")

for item in all_pixels:
    f.write(str(item) + "\n")

f.close()