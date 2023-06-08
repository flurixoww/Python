import cv2
import time
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
pTime = 0

detection = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    #################FPS############################
    # #
    # cTime = time.time()
    # fps = 1/(cTime - pTime) 
    # pTime = cTime

    # cv2.putText(img,f'FPS: {int(fps)}', (40,70), cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
    #####################################################

    hands,img = detection.findHands(img)
    
    lmList, bboxInfo = detection.findHands(img)
    cv2.imshow("Hand", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

