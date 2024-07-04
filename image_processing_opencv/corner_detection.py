import cv2
import matplotlib.pyplot as plt
import numpy as np
"""
image = cv2.imread("su_doku.png",0)
image = np.float32(image)
plt.figure(figsize=(8,5))
plt.imshow(image, cmap="gray")
plt.show()

# cornerHarris

cdt = cv2.cornerHarris(src=image, blockSize=2, ksize=3, k = 0.04)
plt.figure(figsize=(8,5))
plt.imshow(cdt, cmap="gray")
plt.show()

# goodFeaturestoTrack

corners = cv2.goodFeaturesToTrack(image,maxCorners=200, qualityLevel=0.05,
                                  minDistance=10)

corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(image, (x,y), 3, (100,255,255), -1)

plt.figure(figsize=(8,5))
plt.imshow(image)
plt.show()

"""

img = cv2.imread("contour.webp")
"""
plt.figure(figsize=(8,5))
plt.imshow(img, cmap="gray")
plt.show()
"""
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.show()

gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(gray, 170, 255, 0)
plt.imshow(thresh, cmap='gray')
plt.title('Binary Image after Thresholding')
plt.show()


contours, hierarchy = cv2.findContours(thresh,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

image_contour = np.zeros_like(image_rgb)

cv2.drawContours(image_contour, contours, -1, (0,200,150), 3)
plt.imshow(image_contour)
plt.title('Image with Contours')
plt.show()
