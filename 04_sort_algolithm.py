"""
ソートに用いるアルゴリズム
リストを昇順・降順に並べ替える際の計算量・効率について考える。
"""

"""
選択ソート
リストの中から最小の値を見つけ、値をリストの先頭と交換する
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]

for i in range(len(data)):
    min = i
    for j in range(i+1, len(data)):
        if data[min] > data[j]:
            min = j

    data[i],data[min] = data[min], data[i]

print("ソート後：")
print(data)


"""
挿入ソート
データを先頭から順に比較し、格納する位置を見つけて追加する
値はリストの一番後ろにまず格納し、１つずつリストの後ろから順にコピーしていく
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]
for i in range(1, len(data)):
    temp = data[i]
    j = i-1
    while (j>=0) and (data[j] > temp):
        data[j+1] = data[j]
        j-=1

    data[j+1] = temp

print("ソート後：")
print(data)

"""
バブルソート
データが右側の方が小さければ交換する、というタスクを繰り返す。
最小の数が左端・最大の数が右端に行くまでタスクを繰り返すとソートが完了する
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]
for i in range(len(data)):
    #ソートが完了した数を引いた数を引いた分だけループする
    for j in range(len(data)-i-1):
        #右のデータの方が
        if data[j] > data[j+1]:
            data[j], data[j+1]= data[j+1], data[j]

print("ソート後：")
print(data)

"""
ヒープソート
データを先頭・末尾のみから出し入れするスタック・キューとする
最後に格納したデータから順に取り出す→スタック
スタックにデータを格納するのをプッシュ、取り出すことはポップと呼ばれる

"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]
for i in range(len(data)):
    #ソートが完了した数を引いた数を引いた分だけループする
    for j in range(len(data)-i-1):
        #右のデータの方が
        if data[j] > data[j+1]:
            data[j], data[j+1]= data[j+1], data[j]

print("ソート後：")
print(data)
