import cv2
import numpy as np

def detect(frame, model, hands, class_names):
    width, height, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb) # get hand landmark prediction

    className = ''

    # process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for hand_landmarks in result.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                lmx, lmy = int(landmark.x * width), int(landmark.y * height)
                landmarks.append([lmx, lmy])
            # predict gesture in hand gesture recognition model
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            className = class_names[classID]
            if className not in ['thumbs up', 'thumbs down']:
                className = 'none'
    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    return frame, className
