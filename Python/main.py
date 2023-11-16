from absl import app
from absl import flags
from keras.models import load_model
import cv2
import logging
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Local functions
from cv_gesture import detect


FLAGS = flags.FLAGS
curr_directory = '/Users/miller/Projects/Moveocado/Python/'


def main(_):
    # initialize logger
    logger = logging.getLogger("Moveocado")
    logger.setLevel(logging.INFO)

    # initialize the mediapipe hands model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

    # initialize the webcam and get the frame size
    cap = cv2.VideoCapture(0)
    _, img = cap.read()
    height, width, _ = img.shape
    
    # load the gesture recognizer model
    model = load_model(curr_directory + 'data/mp_hand_gesture')
    logger.info("Model loaded")

    # load class names
    with open(curr_directory + 'data/gesture.names', 'r') as f:
        class_names = f.read().split('\n')
    logger.info("Class Names Loaded")
    
    # Video Capture
    while(True): 
        # Capture the video frame by frame 
        ret, img = cap.read() 

        # Flip across y axis
        img = cv2.flip(img, 1)

        # BGR to RGB
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process images
        results = hands.process(rgb_img)

        className = ''
        # if there are hand landmarks
        if results.multi_hand_landmarks:
            landmarks = []
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    h, w, _ = img.shape
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                    landmarks.append([x, y])
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # predict gesture in hand gesture recognition model
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = class_names[classID]
                if className not in ['thumbs up', 'thumbs down']:
                    className = 'none'


            # detect gestures
            # img, gesture = detect(img, model, hands, class_names)

        cv2.putText(img, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the resulting frame 
        cv2.imshow('Hand Tracking', img)
        
        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    # After the loop release the cap object + destroy all the windows
    cap.release() 
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    app.run(main)