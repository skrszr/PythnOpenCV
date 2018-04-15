import cv2
import numpy as np

img = cv2.imread('unnamed.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,255,255),15)

cv2.imshow('image',img)
cv2.waitkey(0)
cv2.destroyAllWindows()
