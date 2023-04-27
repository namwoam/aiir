'''作業二：OpenCV基本應用 提示'''
#載入相關套件模組

buttonDown= False #滑鼠左鍵是否按下(全域面數)

## 自定義滑鼠回應函式
def onMouse(event, x, y, flags, param):

	#如果滑鼠左鍵按下
		global buttonDown
		#buttonDown設為 True
	#如果滑鼠移動
		#如果按鈕按下
			#在(x,y)位置繪製半徑6px的圓形點
            #顯示影像
	#如果滑鼠左鍵彈起
		#buttonDown設為 False
	#如果按下滑鼠右鍵
		#將視窗刪除

  
#    event: EVENT_LBUTTONDOWN,   EVENT_RBUTTONDOWN,   EVENT_MBUTTONDOWN,
#         EVENT_LBUTTONUP,     EVENT_RBUTTONUP,     EVENT_MBUTTONUP,
#         EVENT_LBUTTONDBLCLK, EVENT_RBUTTONDBLCLK, EVENT_MBUTTONDBLCLK,
#         EVENT_MOUSEMOVE: 

#    flags: EVENT_FLAG_CTRLKEY, EVENT_FLAG_SHIFTKEY, EVENT_FLAG_ALTKEY,
#         EVENT_FLAG_LBUTTON, EVENT_FLAG_RBUTTON,  EVENT_FLAG_MBUTTON

## 自定義滑桿回應函式
def onTrackbar(pos):
	#讀取sliders的資料
    #注意slider2(調整size)不得等於0
	#算出im2的寬高
	#讓im1縮小成im2的寬高，縮小後稱為im3
	#建立跟im2一樣大的黑影像im4
	#將im3按slider2(調整size)的比例縮小。縮小後的im3, 貼入im4的中央
    #根據slider1的數值(調整wieght),用cv2.addWeighted對im2與im4加權混合
	#.....
    #顯示影像
        
## 主程式起始處
#建立400x400的黑影像im1
#顯示黑影像
#用cv2.setMouseCallback建立滑鼠回應函式
#等待

# 讀取背景影像im2
# 顯示背景影像
# 用cv2.createTrackbar建立weight滑桿
# 用cv2.createTrackbar建立size滑桿
# 用cv2.createTrackbar建立negative滑桿
# onTrackbar回應函式初始化
# 等待