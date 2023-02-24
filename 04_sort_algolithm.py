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
