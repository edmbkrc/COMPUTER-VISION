import cv2

cap = cv2.VideoCapture(0) # 0---> dahili kamera,   1---> harici kamera

en = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
boy = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"genişlik: {en}\nyükseklik: {boy}")

recorder = cv2.VideoWriter("recording.mp4",
                           cv2.VideoWriter_fourcc(*"XVID"),# *"XVID" = windows için, *"H264" linux ve mac için video baskılama
                           20.0, # kare hızı
                           (en,boy)
                           )

while True:
    ret, frame = cap.read()
    cv2.imshow("KAMERA KAYDI", frame)

    recorder.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("m"):
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()
