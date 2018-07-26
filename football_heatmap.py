# 円を検出する , ヒートマップ(完成版)
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

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
    cv2.imshow('Edited frame', edframe)
    
    #グレーカラーに変更
    gray = cv2.cvtColor(edframe, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    
    #認識の精度を上げるために画像を平滑化
    gray = cv2.GaussianBlur(gray,(33,33),1)
    
    #ピッチの表示イメージ
    pitch = edframe.copy()
    pitch[:,:,:] = [0,101,0] 
    
    #ハフ変換による円検出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 90, param1=35, param2=25, minRadius=0, maxRadius=30)
    if circles != None:
        if len(circles[0]) <= 10 :
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # 囲み線を描く, pitchに描画, ヒートマップ作成
                for j in range(1,21):
                    cv2.circle(pitch,(i[0],i[1]), 2*j ,[0, 0+10*j,255],10)
    cv2.imshow('Heat map circles',pitch)
    
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
