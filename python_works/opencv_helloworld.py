__author__ = 'phaniteja'

# import the necessary packages
import numpy as np
import argparse

import cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
image = cv.LoadImage('steve.jpg', cv.CV_LOAD_IMAGE_COLOR)         # Load the image
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)     # Creates a font
x = 10  # position of text
y = 20  # position of text
cv.PutText(image, "Hello World!!!", (x, y), font, 255)    # Draw the text
cv.ShowImage('a_window', image)    # Show the image

cv.SaveImage('image2.jpg', image)   # Saves the images