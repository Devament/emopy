import cv2
import emopy

# Webcam
cam = cv2.VideoCapture(0)
ret, frame = cam.read()

while ret:
    ret, frame = cam.read()
    faces = emopy.get_faces(frame)
    emotions = emopy.recognize(frame, faces)
    frame = emopy.overlay(frame, faces, emotions)
    cv2.imshow("Preview", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
