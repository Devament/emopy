import numpy as np
import cv2
import dlib
import constants
import os
from keras.models import model_from_json


# Public Functions
def get_faces(frame):
    """
       Identify faces in an image

       :param Mat frame: Image
       :return: Coordinates of faces
       :rtype: list
       """
    dlib_faces = detector(frame, 1)
    faces = []
    if dlib_faces:
        for face in dlib_faces:
            faces += [((
                           max(face.left() - 20, 0),
                           max(face.top() - 20, 0)
                       ),
                       (
                           min(face.right() + 20, frame.shape[1]),
                           min(face.bottom() + 20, frame.shape[0])
                       ))]
    return faces


def overlay(frame, rectangles, text, color=(48, 12, 160)):
    """
       Draw rectangles and text over image

       :param Mat frame: Image
       :param list rectangles: Coordinates of rectangles to draw
       :param list text: List of emotions to write
       :param tuple color: Box and text color
       :return: Most dominant emotion of each face
       :rtype: list
       """

    for i, rectangle in enumerate(rectangles):
        cv2.rectangle(frame, rectangle[0], rectangle[1], color)
        cv2.putText(frame, text[i], (rectangle[0][0] - 10, rectangle[0][1] - 10), cv2.FONT_HERSHEY_DUPLEX, 0.4,
                    color)
    return frame


def recognize(frame, faces):
    """
    Recognize emotion of multiple faces

    :param Mat frame: Image
    :param list faces: Coordinates of faces
    :return: Most dominant emotion of each face
    :rtype: list
    """
    emotions = []
    for face in faces:
        cropped = frame[face[0][1]:face[1][1], face[0][0]:face[1][0]]  # Crop face
        emotions += [__recognize(cropped)]
    return emotions


def __load_models(directory):
    _models = {}
    for item in constants.EMOTIONS:
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), directory)
        json = open(os.path.join(path, constants.EMOTIONS[item] + ".json"))
        _models[item] = model_from_json(json.read())
        json.close()
        _models[item].load_weights(os.path.join(path, constants.EMOTIONS[item] + ".h5"))
    return _models


def __recognize(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    frame = cv2.resize(frame, constants.IMG_SIZE)  # Resize

    # Adjust data for neural net
    frame = np.array([frame])
    frame = frame.reshape(frame.shape[0], 48, 48, 1)
    frame = frame.astype('float32')
    frame /= 255

    predictions = {}
    for model in models:
        predictions[model] = models[model].predict(frame)[0][1]

    # Get emotion with highest value
    emotion = max(predictions, key=predictions.get)

    # Approve emotion if above threshold
    if predictions[emotion] > constants.THRESHOLDS[emotion]:
        return constants.EMOTIONS[emotion]


# Starting Point

# Load models
models = __load_models("models")

# Initialize Dlib's face detector
detector = dlib.get_frontal_face_detector()
