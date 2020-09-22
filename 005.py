import cv2

img = cv2.imread("001.jpg")
blur = cv2.blur(img, (5, 5))

cv2.imwrite('Blur.jpg', blur)
