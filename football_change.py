#合成バージョン
# 円を検出する, 直線で結ぶ , 最大パスコースを数える,　ヒートマップ完成型
import cv2
import numpy as np

def myfunc(i):
    pass # do nothing

cv2.namedWindow('change mode') # create win with win name

cv2.createTrackbar('type', # name of value
                   'change mode', # win name
                   0, # min
                   1, # max
                   myfunc) # callback func

cap = cv2.VideoCapture(0)
maxp = 0
while(True):
    
    v = cv2.getTrackbarPos('type',  # get the value
                           'change mode')  # of the win

    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #サイズを2/3に変更
    frame = cv2.resize(frame, (int(frame.shape[1]*2/3), int(frame.shape[0]*2/3)))
     #赤枠を作成 , 元は(180,80), (674,400), 赤枠の幅を微調整するため
    cv2.rectangle(frame, (177,77), (676,402), (0,0,255), 3) 
    # Display the resulting frame
    cv2.imshow('Raw Frame', frame)
    
    # 窓枠処理をしたframe
    edframe = frame[80:400, 180:674]
    
    #グレーカラーに変更
    gray = cv2.cvtColor(edframe, cv2.COLOR_BGR2GRAY)
    
    #認識の精度を上げるために画像を平滑化
    gray = cv2.GaussianBlur(gray,(33,33),1)
    
    #ピッチの表示イメージ
    pitch = edframe.copy()
    pitch[:,:,:] = [0,101,0] 
    
    # 表示用イメージ
    colimg = edframe.copy()
    
    #ハフ変換による円検出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 90, param1=35, param2=20, minRadius=0, maxRadius=30)
    
    x = 1
    sump = 0
    if circles != None:
        if len(circles[0]) <= 10 :
            circles = np.int16(np.around(circles))#uintをintに変更
            #円の半径の中央値を計算
            y = np.array(circles[0, :, 2])
            median = np.median(y)
            for i in circles[0,:]:

                if(v==0):
                    # 囲み線を描く
                    cv2.circle(colimg,(i[0],i[1]),i[2],(255,255,0),-1)
                    #中心点間の直線を引く
                    for j in circles[0, x:len(circles[0])]:
                        p1 = np.array([i[0],  i[1]])
                        p2 = np.array([j[0],  j[1]])
                        distance = np.linalg.norm(abs(p1-p2))
                        if (distance < median*9): 
                            cv2.line(colimg,(i[0],i[1]),(j[0],j[1]),(0,0,255),2)
                            sump = sump + 1
                    x = x+1

                if(v==1):
                    # 囲み線を描く, pitchに描画, ヒートマップ作成
                    for j in range(1,21):
                        cv2.circle(pitch,(i[0],i[1]), 2*j ,[0, 0+10*j,255],10)

        if sump > maxp:
            maxp = sump
    
    if(v==0):
        cv2.imshow('detected circles',colimg)
    elif (v==1):
        cv2.imshow('detected circles',pitch)
    
    if cv2.waitKey(1) == 27:
        print("最大パスコース数: ", maxp)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
