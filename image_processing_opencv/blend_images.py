import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("landscape1.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(15, 15))
plt.title("landscape1")
plt.imshow(img1)
plt.show()


img2 = cv2.imread("landscape2.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()

img3 = cv2.imread("landscape3.png")
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img3 = cv2.resize(img3, (1000, 600) )
plt.imshow(img3)
plt.show()


print(f"shape of img1: {img1.shape}\nshape of img2: {img2.shape}\nshape of img3: {img3.shape}")


blended_landscapes = cv2.addWeighted(src1=img1, alpha=0.3, src2=img2, beta=0.7, gamma=0)

plt.figure(figsize=(15, 15))
plt.imshow(blended_landscapes)
plt.show()
