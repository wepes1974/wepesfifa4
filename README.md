## 概要 
サッカー, フォーメーションから見るパスコース・ヒートマップ図を表示させるコード

football_pass.pyではパスコース, 

football_heatmap.pyではヒートマップをそれぞれ表示させる

football_change.py　では2つの処理を切り替えられるようにした. 切り替えは別ウインドのパラメータで行う

## 実装した処理

[パスコース] ハフ変換より画像から, 丸を検出し, 適当な丸の距離を線で結ぶ. 距離のしきい値は中央値によって定める

[ヒートマップ] 検出した丸の中心から小さな円を連続して描き, ヒートマップに見立てる.　
  
