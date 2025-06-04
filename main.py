from absl import app
from tensorflow.keras.models import load_model
import cv2
import logging
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pyautogui

from cv_button import Button
from cv_keyboard import Keyboard
from cv_gesture import detect


def main(_):
    # Initialize the logger
    logger = logging.getLogger("moveocado")
    logger.setLevel(logging.INFO)

    # Initialize Mediapipe Hand model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

    # Initialize the webcam and get the width and height
    cap = cv2.VideoCapture(0)
    _, img = cap.read()
    height, width, _ = img.shape

    # Load the gesture recognizer model
    model = load_model('data/mp_hand_gesture')

    # Load class names
    with open('data/gesture.names', 'r') as f:
        classNames = f.read().split('\n')

    cooldown = 10
    while True:
        # Read the image from the webcam
        success, img = cap.read()

        # Flip the image horizontally to create a mirror effect
        img = cv2.flip(img, 1)

        # Convert the image to RGB (MediaPipe requires RGB input)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image to detect hands
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the image
                for landmark in hand_landmarks.landmark:
                    h, w, _ = img.shape
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                mp_drawing.draw_landmarks(img,
                                          hand_landmarks,
                                          mp_hands.HAND_CONNECTIONS)

                # Check pointer finger position to move left and right
                if hand_landmarks.landmark[8]:
                    if hand_landmarks.landmark[8].x < 0.075:
                        pyautogui.press('left')
                    if hand_landmarks.landmark[8].x > 0.925:
                        pyautogui.press('right')


        # Detect gestures
        img, gesture = detect(img, model, hands, classNames)
        if gesture:
            logger.info(gesture)

        # Check gestures to rotate and move down
        cooldown = max(0, cooldown - 1)
        if gesture == 'thumbs down' and cooldown == 0:
            pyautogui.press('down')
            cooldown = 10
        if gesture == 'thumbs up' and cooldown == 0:
            pyautogui.press('up')
            cooldown = 10

        # Display the image with hand landmarks
        cv2.imshow("Hand Tracking", img)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    app.run(main)