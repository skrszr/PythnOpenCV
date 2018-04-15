import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('unnamed.jpg',cv2.IMREAD_GRAYSCALE)

##cv2.imshow('marmara kevser',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([120,227],[159,159],'a',linewidth=8)
plt.show()
