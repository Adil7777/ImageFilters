import cv2

img = cv2.imread("001.jpg")
dst = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

cv2.imwrite('Details.jpg', dst)
