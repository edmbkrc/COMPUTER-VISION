import cv2
import matplotlib.pyplot as plt

image = cv2.imread("landscape1.png") # BGR
"""
cv2.imshow("MANZARA", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(15,8))
plt.imshow(image_gray, cmap="gray") # RGB
plt.title("MANZARA")
plt.xlabel("GENISLIK")
plt.ylabel("YÜKSEKLİK")
plt.show()

thresold, image_threshold = cv2.threshold(image_gray, thresh=60, maxval=255,
                                          type=cv2.THRESH_BINARY)#THRESH_BINARY_INV

plt.imshow(image_threshold, cmap="gray")
plt.show()

img_threshold = cv2.adaptiveThreshold(image_gray, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY,
                                      15, # 15*15 piksellik alan
                                      3
                                      )

plt.imshow(img_threshold, cmap="gray")
plt.show()