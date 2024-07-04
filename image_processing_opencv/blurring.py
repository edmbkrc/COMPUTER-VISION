import cv2
import matplotlib.pyplot as plt
"""
image = cv2.imread("landscape1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,5))
plt.title("ORMAN-GOL")
plt.xlabel("GENISLIK")
plt.ylabel("YUKSEKLIK")
plt.imshow(image)
plt.show()

# ortalama yöntemi ile bulanıklaştırma

blurred1 = cv2.blur(image, (5,5))
plt.figure(figsize=(8,5))
plt.title("BLURRED IMAGE")
plt.imshow(blurred1)
plt.show()

# median yöntemi ile bulanıklaştırma
blurred2 = cv2.medianBlur(image, ksize=5) # tek sayı kullanılmalı
plt.figure(figsize=(8,5))
plt.title("MEDIAN BLURRED IMAGE")
plt.imshow(blurred2)
plt.show()

# Gaussian yöntemi ile bulanıklaştırma
blurred3 = cv2.GaussianBlur(image, (5,5), 0) # 0, standart sapmayı opencv tarafından yapılmasını sağlar
plt.figure(figsize=(8,5))
plt.title("GAUSSIAN BLURRED IMAGE")
plt.imshow(blurred3)
plt.show()
"""
# gradients
image = cv2.imread("su_doku.png",0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,5))
plt.title("SUDOKU")
plt.axis("off")
plt.imshow(image, cmap="gray")
plt.show()

x = cv2.Sobel(src=image, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure(figsize=(8,5))
plt.title("SUDOKU X")
plt.axis("off")
plt.imshow(x, cmap="gray")
plt.show()

y = cv2.Sobel(src=image, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(figsize=(8,5))
plt.title("SUDOKU Y")
plt.axis("off")
plt.imshow(y, cmap="gray")
plt.show()

laplacian = cv2.Laplacian(image, ddepth=cv2.CV_16S, ksize=5)
plt.figure(figsize=(8,5))
plt.title("SUDOKU-LAPLACIAN")
plt.axis("off")
plt.imshow(laplacian, cmap="gray")
plt.show()