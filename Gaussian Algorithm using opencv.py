import numpy as np
import cv2  as cv

img = cv.imread('noisyimg.png', 0)
new_img = cv.GaussianBlur(img, (5, 5), 0)

cv.imshow('Image', img)
cv.imshow('New Image', new_img)

k = cv.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('new_image.png',new_img)
    cv.destroyAllWindows()