import cv2
from cvzone.FaceMeshModule import FaceMeshDetector




cap = cv2.VideoCapture(0)
detection = FaceMeshDetector(maxFaces=2)
cap.set(3, 1280)
cap.set(4, 960)

while True:

    succes, img = cap.read()
    img, faces = detection.findFaceMesh(img)

    if faces:
        print(faces[0])
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



