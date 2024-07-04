import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("watershed_coins.webp")
plt.figure(figsize=(8,5))
plt.imshow(img)
plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap="gray")
plt.show()

# blurring---bulanıklaştırma
blurred_coin = cv2.GaussianBlur(gray, (11,11), 0)
plt.imshow(blurred_coin, cmap="gray")
plt.show()


# threshold---eşik dğer atama
ret, thresh_coin = cv2.threshold(blurred_coin, 70,255, cv2.THRESH_BINARY)
plt.imshow(thresh_coin, cmap="gray")
plt.show()

#opening
kernel = np.ones((3,3),np.uint8)
plt.imshow(kernel, cmap="gray"),plt.show()
opening = cv2.morphologyEx(thresh_coin,cv2.MORPH_OPEN, kernel, iterations=2)
plt.imshow(opening, cmap="gray"),plt.show()

#mesafe dönüşümü
dist = cv2.distanceTransform(opening, cv2.DIST_L2, maskSize=5)
plt.imshow(dist, cmap="gray"),plt.show()

#threshold
ret, threshold2 = cv2.threshold(dist, 0.4*np.max(dist),255,0)
plt.imshow(threshold2, cmap="gray"),plt.show()

# dilating
dilated = cv2.dilate(opening, kernel, iterations=1)
threshold2 = np.uint8(threshold2)
subtracted = cv2.subtract(dilated,threshold2)
plt.imshow(subtracted, cmap="gray"),plt.show()

#connection

ret, marker = cv2.connectedComponents(threshold2)
marker = marker + 1
marker[subtracted==255] = 0
plt.imshow(marker, cmap="gray"),plt.show()

# watershed
marker = cv2.watershed(img,marker)
plt.imshow(marker, cmap="gray"),plt.show()

# contour
contours, hierarchy = cv2.findContours(thresh_coin.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(img, contours, i, (255, 255, 0), 2)

plt.imshow(img), plt.show()