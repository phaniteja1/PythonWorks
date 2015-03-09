__author__ = 'phaniteja'

# This file is to apply operations on each pixel of the file

# Import the modules to perform operations on Image - PIL is used for operations
from PIL import Image


try:
    # Load an image from the hard drive
    original = Image.open("steve.jpg")

except FileNotFoundError:
    print("Unable to load image")


# Apply pixel transformations
edited_region = original.point(lambda i: i * 1.5)

# Display both images
original.show()
edited_region.show()

# save the new image
# edited_region.save("edited.png")
