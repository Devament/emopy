import cv2
import emopy

for i in range(1, 4):
    frame = cv2.imread('imgs/' + str(i) + '.jpg')
    faces = emopy.get_faces(frame)
    emotions = emopy.recognize(frame, faces)
    frame = emopy.overlay(frame, faces, emotions)
    cv2.imshow("Preview", frame)
    cv2.waitKey(0)
