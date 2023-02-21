"""
計算コストや実行時間を考慮したアルゴリズム
「良い」アルゴリズムとはデータ量に対する計算コスト・実行時間が少ないアルゴリズムを指す。
例えばフィボナッチ数の計算などではメモ化を活用した方が良いアルゴリズムとなる。

環境・言語に依存せずにアルゴリズムを評価する指標として、「計算量」が用いられる。

時間計算量 - 処理にかかる時間
空間計算量 - 処理に要する記憶容量

メモ化を活用すると時間計算量が減る代わりに、処理に要する空間計算量が増える場合もある。

入力量にたいする計算量の増分を自然対数・指数などで表現する記法を、オーダー記法という。
複数のアルゴリズムを検討する際、どれが効率が良いかを大雑把に検定できる

オーダーの比較

O(1) - リスト・コレクション等へのアクセス
O(logn) - 二分探索
O(n) - 線形探索
O(n*logn) - マージソート、ヒープソート
O(n^2) - 選択ソート、挿入ソート、バブルソート、シェルソート
O(n^3) - 行列の掛け算
O(2^n) - ナップサック問題
O(n!) - 巡回セールスマン問題

計算量に関してより詳細に学びたい場合は、チューリングマシン等の情報科学に関して学ぶ

アルゴリズムの計算量を考える際は、最も処理に時間がかかるデータの処理＝最悪計算量,
もしくは最悪計算量になるケースが少ない場合は平均計算量を基準とする。


"""

for i in range(1,100):
    #論理的に排他的となるものの優先度を高めに設定する
    if (i%3==0 and i%5==0):
        print(str(i) + ":FizzBuzz")
    elif (i%3==0):
        print(str(i) + ":Fizz")
    elif (i%5==0):
        print(str(i) + ":Buzz")
    else:
        print(i)