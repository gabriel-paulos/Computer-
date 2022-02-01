import numpy as np
import cv2

import math
import pyautogui

def draw_Rectangles(frame):

    rows,cols,_ = frame.shape
    
    hand_rect_one_x = np.array(
        [6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,
         12 * rows / 20, 12 * rows / 20], dtype=np.uint32)

    hand_rect_one_y = np.array(
        [9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,
         10 * cols / 20, 11 * cols / 20], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10

    total_size = hand_rect_one_x.shape[0]
    
    for i in range(total_size):
        cv2.rectangle(frame, (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (0, 255, 0), 1)

    return frame,[hand_rect_one_x,hand_rect_one_y]

def hand_histogram(frame, total_size, hand_rect):
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    roi = np.zeros([90, 10, 3], dtype=hsv.dtype)

    for i in range(total_size):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv[hand_rect[0][i]:hand_rect[0][i] + 10,
                                          hand_rect[1][i]:hand_rect[1][i] + 10]

    hist= cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

    return hist

def main():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        draw = draw_Rectangles(frame)
        hist = hand_histogram(draw)

        if cv2.waitKey(1) == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()

if __name__ = '__main__':
    main()