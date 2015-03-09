__author__ = 'phaniteja'

# Import the modules to perform operations on Image - PIL is used for operations

from PIL import Image


try:
    # Load an image from the hard drive
    original = Image.open("steve.jpg")

except FileNotFoundError:
    print("Unable to load image")

# Creating a cropped_region by defining a box

width, height = original.size   # Get dimensions
left = width // 4
top = height // 4
right = 3 * width // 4
bottom = 3 * height // 4

box = (left, top, right, bottom)
cropped_region = original.crop(box)

# Apply pixel transformations
cropped_region = cropped_region.point(lambda i: i * 1.2)

# Display both images
original.show()
cropped_region.show()

# save the new image
cropped_region.save("region.png")
