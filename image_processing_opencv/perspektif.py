import cv2
import numpy as np

phone = cv2.imread("phone.png")
cv2.imshow("IPHONE",phone)

width, height = 250,350

limits = np.float64([[450, 109],[226, 356],[572, 222],[352, 480]])
new_image = np.float64([[0,0],[0,height],[width,0],[width,height]])

transform_image = cv2.getPerspectiveTransform(limits,new_image)
print(transform_image)

result = cv2.warpPerspective(phone,transform_image, (width, height))

cv2.imshow("Perspektif Resmi", result)


cv2.waitKey(0)
cv2.destroyAllWindows()


