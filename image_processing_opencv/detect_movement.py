"""
import cv2

cap = cv2.VideoCapture(0)

ret1, frame1 = cap.read()
ret2 ,frame2 = cap.read()

while True:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    frame1_blur = cv2.GaussianBlur(frame1_gray, (11,11), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (11,11), 0)

    diff = cv2.absdiff(frame1_blur, frame2_blur)
    cv2.imshow("Movement", diff)

    frame1 = frame2

    ret, frame2 = cap.read()

    if not ret:
        cap.release()
        break
    key = cv2.waitKey(1)
    if key == ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()



import cv2

cap = cv2.VideoCapture("cars.mp4")

ret1, frame1 = cap.read()
ret2 ,frame2 = cap.read()

while True:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    frame1_blur = cv2.GaussianBlur(frame1_gray, (11,11), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (11,11), 0)

    diff = cv2.absdiff(frame1_blur, frame2_blur)
    cv2.imshow("Movement", diff)

    frame1 = frame2

    ret, frame2 = cap.read()

    if not ret:
        cap.release()
        break
    key = cv2.waitKey(1)
    if key == ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()



import cv2

cap = cv2.VideoCapture("airplanes.mp4")

ret1, frame1 = cap.read()
ret2 ,frame2 = cap.read()

while True:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    frame1_blur = cv2.GaussianBlur(frame1_gray, (11,11), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (11,11), 0)

    diff = cv2.absdiff(frame1_blur, frame2_blur)
    cv2.imshow("Movement", diff)

    frame1 = frame2

    ret, frame2 = cap.read()

    if not ret:
        cap.release()
        break
    key = cv2.waitKey(1)
    if key == ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("cars.mp4")

ret1, frame1 = cap.read()
ret2 ,frame2 = cap.read()

while True:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    frame1_blur = cv2.GaussianBlur(frame1_gray, (11,11), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (11,11), 0)

    diff = cv2.absdiff(frame1_blur, frame2_blur)

    thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    final = cv2.dilate(thresh, None, iterations=2)

    masked = cv2.bitwise_and(frame1, frame1, mask=thresh)
    white_pixels = np.sum(thresh) / 255

    rows, cols = thresh.shape
    total = rows * cols

    if white_pixels > 0.01*total:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame1, "Movement Detected--Hareket tespit edildi", (10,50), font, 1,  (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("Motion", frame1)

    frame1 = frame2

    ret, frame2 = cap.read()

    if not ret:
        cap.release()
        break
    key = cv2.waitKey(1)
    if key == ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()

