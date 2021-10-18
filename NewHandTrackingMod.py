import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


ptime = 0
ctime = 0
capture = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = capture.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)





