# 円を検出する, 直線で結ぶ , 最大パスコースを数える, 完成型
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
maxp = 0
while(True):

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
        
        if sump > maxp:
            maxp = sump
    cv2.imshow('detected circles',colimg)
    
    if cv2.waitKey(1) == 27:
        print("最大パスコース数: ", maxp)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
