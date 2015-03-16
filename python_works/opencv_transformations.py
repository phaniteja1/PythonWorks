import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('images/coke1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/coke_temp3.jpg', 0)
w, h = template.shape[::-1]

count = 0

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    count = (count + 1)

print("Number of cokes : " + str(count/1000))
cv2.imwrite('images/res.png', img_rgb)

