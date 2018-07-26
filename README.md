## 概要 
サッカー, フォーメーションから見るパスコース・ヒートマップ図を表示させるコード

football_pass.pyではパスコース, 

football_heatmap.pyではヒートマップをそれぞれ表示させる

football_change.py　では2つの処理を切り替えられるようにした. 切り替えは別ウインドのパラメータで行う

## 実装した処理

[パスコース] ハフ変換より画像から, 丸を検出し, 適当な丸の距離を線で結ぶ. 距離のしきい値は中央値によって定める

[ヒートマップ] 検出した丸の中心から小さな円を連続して描き, ヒートマップに見立てる.　
  
## 実行環境

macOS High Sierra バージョン10.13.5 , Python 3.6.5 , OpenCV 3.4.1

## 参考サイト

EditFrameの表示の仕方 2つのフレーム表示

http://ensekitt.hatenablog.com/entry/2017/12/19/200000



枠の表示・切り抜かれる部分の表示

https://qiita.com/EN-0/items/784b919ea0c090871a08


https://algorithm.joho.info/programming/python/opencv-roi-py/



OpenCVの描画機能

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html



画像の平滑化

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_filtering/py_filtering.html



ハフ変換による円検出

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html


良いパラメータの例

http://www.digifie.jp/blog/archives/1438


パラメータ解説

http://robonchu.hatenablog.com/entry/2017/08/21/163135



点間の距離を求める

https://teratail.com/questions/105400

https://tokibito.hatenablog.com/entry/20121222/1356187172

http://programming.blogo.jp/python/numpy/%E3%83%8E%E3%83%AB%E3%83%A0


芝生の色

http://pluscolorn.sub.jp/rgbseachtest3_1.php?1id=61

