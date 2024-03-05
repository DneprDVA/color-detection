import cv2
import numpy as np

img = cv2.imread('exp-img/img-0.jpg', 0)

ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
eroded = cv2. erode(thresh, kernel, iterations=1)
dilated = cv2.dilate(eroded, kernel, iterations=1)

mask = dilated == 255

# cv2.imshow(mask)
cv2.imshow('Хорда сегмента', img)
# cv2.imshow('Хорда сегмента', thresh)

cv2.waitKey(0) 
cv2.destroyAllWindows() 