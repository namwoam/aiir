'''作業二：OpenCV基本應用 提示'''
# 載入相關套件模組

import cv2
import numpy as np
import os

buttonDown = False  # 滑鼠左鍵是否按下(全域面數)
show_display = True
# 自定義滑鼠回應函式


def onMouse(event, x, y, flags, param):

    # 如果滑鼠左鍵按下
    global buttonDown, show_display
    if event == cv2.EVENT_LBUTTONDOWN:
        buttonDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        buttonDown = False
    if event == cv2.EVENT_MOUSEMOVE and buttonDown:
        circle_color = (0, 255, 255)  # Yellow
        cv2.circle(im1, (x, y), 6, circle_color, 12)
    cv2.imshow("draw", im1)
    if event == cv2.EVENT_RBUTTONDOWN:
        # cv2.destroyWindow("draw") in callback function will cause segment fault
        show_display = False
    # buttonDown設為 True
    # 如果滑鼠移動
    # 如果按鈕按下
    # 在(x,y)位置繪製半徑6px的圓形點
# 顯示影像
    # 如果滑鼠左鍵彈起
    # buttonDown設為 False
    # 如果按下滑鼠右鍵
    # 將視窗刪除


#    event: EVENT_LBUTTONDOWN,   EVENT_RBUTTONDOWN,   EVENT_MBUTTONDOWN,
#         EVENT_LBUTTONUP,     EVENT_RBUTTONUP,     EVENT_MBUTTONUP,
#         EVENT_LBUTTONDBLCLK, EVENT_RBUTTONDBLCLK, EVENT_MBUTTONDBLCLK,
#         EVENT_MOUSEMOVE:

#    flags: EVENT_FLAG_CTRLKEY, EVENT_FLAG_SHIFTKEY, EVENT_FLAG_ALTKEY,
#         EVENT_FLAG_LBUTTON, EVENT_FLAG_RBUTTON,  EVENT_FLAG_MBUTTON
    pass
# 自定義滑桿回應函式


def onTrackbar(pos):
    weight = cv2.getTrackbarPos("weight", "fusion")
    size = cv2.getTrackbarPos("size", "fusion")
    if size == 0:
        # terminate if size is 0
        return
    negative = cv2.getTrackbarPos("negative", "fusion")
    print("trackbar:", weight, size, negative)
    # 讀取sliders的資料
    # 注意slider2(調整size)不得等於0
    # 算出im2的寬高
    # 讓im1縮小成im2的寬高，縮小後稱為im3
    drawing_size = (min(im2.shape[1], im2.shape[0]),
                    min(im2.shape[1], im2.shape[0]))
    im3 = cv2.resize(im1, drawing_size)
    im4 = np.zeros(im2.shape, np.uint8)
    resized_drawing_size = (im3.shape[0]*size//100, im3.shape[1]*size//100)
    im3 = cv2.resize(im3, resized_drawing_size)
    cx, cy = im4.shape[0]//2, im4.shape[1]//2
    dx, dy = im3.shape[0]//2, im3.shape[1]//2
    im4[cx-dx:cx-dx+im3.shape[0], cy-dy:cy-dy+im3.shape[1]] = im3
    im5 = cv2.addWeighted(im4, weight/100, im2, 1-weight/100, 0.0)
    # im5 is the weighted result of drawing and background
    negative_range = (im5.shape[0], im5.shape[1]*negative//100)
    # get the portion of the image to be nverted
    im5[0:negative_range[0], 0:negative_range[1]] = 255 - \
        im5[0:negative_range[0], 0:negative_range[1]]
    # invert the negative_range region in im5
    cv2.imshow("fusion", im5)
    # 建立跟im2一樣大的黑影像im4
    # 將im3按slider2(調整size)的比例縮小。縮小後的im3, 貼入im4的中央
    # 根據slider1的數值(調整wieght),用cv2.addWeighted對im2與im4加權混合
    # .....
    # 顯示影像

    # 主程式起始處
    # 建立400x400的黑影像im1
    pass


def resetTrackbar():
    cv2.setTrackbarPos('weight', 'fusion', 50)
    cv2.setTrackbarPos('size', 'fusion', 50)
    cv2.setTrackbarPos('negative', 'fusion', 0)
    # function for reset all the trackbars


cv2.namedWindow("draw", cv2.WINDOW_GUI_NORMAL)
im1 = np.zeros((400, 400, 3), np.uint8)
cv2.imshow("draw", im1)
cv2.resizeWindow("draw", im1.shape[1], im1.shape[0])
cv2.setMouseCallback("draw", onMouse)
while True:
    cv2.waitKey(10)
    if show_display == False:
        cv2.destroyWindow("draw")
        break
# 顯示黑影像
# 用cv2.setMouseCallback建立滑鼠回應函式
# 等待

cv2.namedWindow("fusion")
background_file = "background.png"
im2 = cv2.imread(os.path.join(os.path.dirname(__file__),  background_file))
cv2.imshow("fusion", im2)
cv2.resizeWindow("fusion", im2.shape[1], im2.shape[0])
# 讀取背景影像im2
# 顯示背景影像
cv2.createTrackbar('weight', 'fusion', 0, 100, onTrackbar)
cv2.createTrackbar('size', 'fusion', 0, 100, onTrackbar)
cv2.createTrackbar('negative', 'fusion', 0, 100, onTrackbar)
resetTrackbar()
# 用cv2.createTrackbar建立weight滑桿
# 用cv2.createTrackbar建立size滑桿
# 用cv2.createTrackbar建立negative滑桿
# onTrackbar回應函式初始化
# 等待
while True:
    key = cv2.waitKey(10)
    if (key & 0xFF) == 27:  # code for ESC
        cv2.destroyWindow("fusion")
        break
    elif (key & 0xFF) == ord("r"):
        resetTrackbar()
