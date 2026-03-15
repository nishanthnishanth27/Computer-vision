import cv2
import mediapipe as mp
import pyautogui

# AI Hand tracking setup
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = cap.read()
        frame = cv2.flip(frame, 1) # Mirror effect
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output = hand_detector.process(rgb_frame)
                    hands = output.multi_hand_landmarks

                        if hands:
                                for hand in hands:
                                            landmarks = hand.landmark
                                                        for id, landmark in enumerate(landmarks):
                                                                        # Index finger point
                                                                                        if id == 8:
                                                                                                            x = int(landmark.x * screen_width)
                                                                                                                                y = int(landmark.y * screen_height)
                                                                                                                                                    pyautogui.moveTo(x, y) # Moves the mouse!

                                                                                                                                                        cv2.imshow('AI Virtual Mouse', frame)
                                                                                                                                                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                                                                                                                                                    break
                                                                                                                                                                    cap.release()
                                                                                                                                                                    cv2.closeAllWindows()
                                                                                                                                                                    