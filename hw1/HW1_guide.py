#作業1: python, np, plt 繪圖應用
#載入相關套件模組

#輸入影像檔名字串 filename (用 input)

## Part 1: 繪製 Colorbars ################
#生成0~255的一維整數陣列a (用 numpy)
#格式改為uint8 (用 astype)
#a重複3次，長度成為256*3的b陣列 (用 repeat)
#建立(64*8,256*3,3)大小的零矩陣c，格式是uint8

#用兩層for迴圈產生影像資訊：第一層跟高有關，第二層跟RGB通道有關
    #將b複製到c矩陣特定掃描線與色通道
    #可用np.invert將陣列b的順序倒置

#建立1號視窗(用 figure)
#顯示影像c(用 imshow)
#加標題
#不顯示 x,y 軸刻度值
#暫停2秒(用 pause)
#關閉1號視窗(用 close)

## Part 2: 繪製黑白圈圈圖 #################
## 自訂一個函數，名稱是 radius，輸入u,v影像座標，算出(return)遠離中心的半徑

#產生一個6至1之間，以-0.2為間隔的數列d
#將d開平方，再用cumsum產生半徑的門檻值數列e
#以float32格式，建立512x512大小的零矩陣f

#利用雙層for迴圈，窮舉x,y影像座標
    #用radius函式計算遠離影像中心的半徑r，x,y要先減去255
    #用for迴圈，依序查詢數列e裡的數值
        #如果r大於數列e裡的第z筆數值，就用變數idx記錄該索引值z，並用(break)離開for迴圈
    #將idx值取除以2的餘數，將該數值存入影像f的x,y位置

#建立2號視窗(用 figure)
#顯示影像f，色彩對用表用'gray'(用 imshow, 以及cmap參數)
#加標題
#水平軸刻度用0~512, 以64為間隔(用 xtick)
#垂直軸刻度用0~512, 以64為間隔(用 ytick)
#暫停2秒(用 pause)
#關閉2號視窗(用 close)

## Part 3: 6種影像處理之水平拼接圖像，隨機排序+輪播 #########
## 自訂一個函數，名稱是 process
## 輸入正方形彩色影像(im_in)以及影像處理選項p
## 根據選項 p, 將處理後的影像(im_out)輸出(return)
## 可以考慮的處理有 rot90, fliplr, flipud, bitwise_not, clip, where 等等
def process(im_in, p):
    if p==0:
       ...
    elif p==1:
       ...
    return im_out

#主程式進入點
#讀取 filename 指定的彩色影像im1 (用 plt.imread)
#讀取該影像的高(h)/寬(w)/通道數(ch) (用.shape)
#取影像im1的局部，使im2的高寬都是h
#建立uint8格式的四維零陣列，尺寸是(6,h,h,ch)
#建立一個 for 迴圈，分別把 process 產生的6種影像，存到im3裡
    #im3的第一維就是process的選項

#用 for 迴圈跑五次隨機順序排列的影像im4
    #用np.random.permutation(6)產生0~5的隨機序列
    #用 hstack, 以g的順序，水平合併6個子圖
    
    #建立3號視窗(用 figure)
    #顯示影像im4(用 imshow)
    #加標題(含隨機次數)
    #不顯示 x,y 軸刻度值
    #暫停1秒
#將im4存入'HW1.jpg'檔
#關閉3號視窗(用 close)

## Part 4: 將最後的6個子圖，以2x3圖形陣列(用add_subplot)，全螢幕顯示 ####
#建立4號視窗(用 figure)
#建立 for 迴圈，依序處理圖形陣列中的6個圖
    #添加2x3圖形陣列的第i+1個子圖
    #讀取im3中g[i]序號所對映的子影像，並用squeeze降成三維，存入im5
    #顯示影像im5
    #顯示子圖的標題
    #不顯示 x,y 軸刻度值

#全螢幕顯示
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show() #顯示




