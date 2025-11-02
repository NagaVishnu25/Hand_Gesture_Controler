import cv2
import mediapipe as mp
import pyautogui
import time
import math
import keyboard

pyautogui.FAILSAFE = False
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
wScr, hScr = pyautogui.size()
pTime = 0
last_double_click_time = 0
double_click_delay = 0.5
last_click_time = 0

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        lmList = []

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))
                mp_drawing.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)

        if len(lmList) >= 21:
            x1, y1 = lmList[8][1], lmList[8][2]
            x2, y2 = lmList[12][1], lmList[12][2]
            fingers_up = [
                lmList[8][2] < lmList[6][2],
                lmList[12][2] < lmList[10][2],
                lmList[16][2] < lmList[14][2],
                lmList[20][2] < lmList[18][2]
            ]

            if fingers_up[0] and not any(fingers_up[1:]):
                pyautogui.moveTo((x1 / image.shape[1]) * wScr, (y1 / image.shape[0]) * hScr)

            if distance(lmList[8][1:], lmList[4][1:]) < 30:
                current_time = time.time()
                if current_time - last_click_time > 0.5:
                    pyautogui.click()
                    last_click_time = current_time

            if distance(lmList[8][1:], lmList[12][1:]) < 30:
                current_time = time.time()
                if current_time - last_double_click_time > double_click_delay:
                    pyautogui.doubleClick()
                    last_double_click_time = current_time

            if fingers_up[0] and fingers_up[1] and not any(fingers_up[2:]):
                pyautogui.scroll(30)

            if fingers_up[1] and fingers_up[2] and not fingers_up[0] and not fingers_up[3]:
                pyautogui.scroll(-30)

        if keyboard.is_pressed("esc"):
            print("Exiting...")
            break

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Gesture Controller", image)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
