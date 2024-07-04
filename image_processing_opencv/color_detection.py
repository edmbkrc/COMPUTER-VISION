import cv2
import numpy as np
from collections import deque

#HSV----Hue, Saturate, Value

buffer_size = 16
pts = deque(maxlen=buffer_size)

blue_lower = (84, 98, 0)
blue_upper = (179, 255, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

while True:
    ret, image_original = cap.read()

    if ret:
        #blurring
        blurred = cv2.GaussianBlur(image_original, (11,11), 0)

        # hsv çevirme
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", hsv)

        # maske oluşturma
        mask = cv2.inRange(hsv, blue_lower, blue_upper)
        cv2.imshow("MASKE", mask)

        #gürültme azaltma
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("GURULTUSUZ",mask)

        mask2 = cv2.bitwise_and(image_original, image_original, mask=mask)
        cv2.imshow("MASK2", mask2)

        # kontur işlemleri
        (contours, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>0:
            c = max(contours, key=cv2.contourArea)
            rect = cv2.minAreaRect(c)
            ((x,y), (width,height), rotation)=rect

            # kutucuk
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            #moment
            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

            # kontur çizdirme
            cv2.drawContours(image_original, [box], 0, [0,255,255], 2)

            #daire çizme
            cv2.circle(image_original, center, 5, (255, 0, 255), -1)

            # yazı yazma
            cv2.putText(image_original, "HSV", (200,100), cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,150))

        pts.append(center)
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None: continue
            cv2.line(image_original, pts[i - 1], pts[i], (90, 90, 255), 3)

        cv2.imshow("COLOR DETECTION", image_original)


    if cv2.waitKey(1) & 0XFF == ord("q"):break

cap.release()
cv2.destroyAllWindows()

