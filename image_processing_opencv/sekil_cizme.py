import cv2
import numpy as np

img  = np.zeros((600, 800, 3), np.uint8)


cv2.line(img,(0,0),(800,600),(255,0,0),5)
cv2.imshow("LINE",img)

cv2.rectangle(img, (100,100),(600,600),(255,0,255),-1)
cv2.imshow("RECTANGLE",img)

cv2.circle(img,(400,300),200,(255,255,0),cv2.FILLED)
cv2.imshow("CIRCLE",img)

cv2.putText(img, "YAPAY ZEKA", (100,100),
            cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,150))
cv2.imshow("METIN",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

