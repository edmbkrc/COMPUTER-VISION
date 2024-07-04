import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)

ret, frame = cap.read()

if ret == False:
    print("Kamera bulunamadı...")

x, y, width, height = 300, 200, 200, 200
track_window = (x, y, width, height)

# region of interest ---- ilgi alanı bölgesi
roi = frame[y:y+height, x:x+width]

# hsv---hue, saturate, values renk, doygunluk,
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0,180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    x, y, w, h = track_window
    img2 = cv2.rectangle(frame, (x,y), (x+w, y+h), 255, 3)
    cv2.imshow("Meanshift Tracking", img2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


