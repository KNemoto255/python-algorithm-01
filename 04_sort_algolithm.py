"""
ソートに用いるアルゴリズム
リストを昇順・降順に並べ替える際の計算量・効率について考える。
・選択ソート
・挿入ソート
・バブルソート
・ヒープソート
・マージソート
・クイックソート

"""

"""
選択ソート
リストの中から最小の値を見つけ、値をリストの先頭と交換する
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
#実際に何回処理が行われたかをいカウントする
data = [6,15,4,2,8,5,11,9,7,13]
calcurated = 0

for i in range(len(data)):
    min = i
    for j in range(i+1, len(data)):
        if data[min] > data[j]:
            min = j
            calcurated += 1

    data[i],data[min] = data[min], data[i]

print("ソート後：")
print(data)
print("処理回数：")
print(calcurated)


"""
挿入ソート
データを先頭から順に比較し、格納する位置を見つけて追加する
値はリストの一番後ろにまず格納し、１つずつリストの後ろから順にコピーしていく
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]
calcurated = 0

for i in range(1, len(data)):
    temp = data[i]
    j = i-1
    while (j>=0) and (data[j] > temp):
        data[j+1] = data[j]
        j-=1
        calcurated += 1

    data[j+1] = temp

print("ソート後：")
print(data)
print("処理回数：")
print(calcurated)


"""
バブルソート
データが右側の方が小さければ左側と交換する、というタスクを繰り返す。
最小の数が左端・最大の数が右端に行くまでタスクを繰り返すとソートが完了する
O(n^2)
"""
#先頭のインデックスから調べていき、徐々に後ろの方に範囲を狭める
data = [6,15,4,2,8,5,11,9,7,13]
calcurated = 0

for i in range(len(data)):
    #ソートが完了した数を引いた数を引いた分だけループする
    for j in range(len(data)-i-1):
        #右のデータの方が小さければ、左と交換する
        if data[j] > data[j+1]:
            data[j], data[j+1]= data[j+1], data[j]
            calcurated += 1

print("ソート後：")
print(data)
print("処理回数：")
print(calcurated)


"""
ヒープソート
データを先頭・末尾のみから出し入れするリスト＝スタック・キューとする。
データの格納方式を制限することで、途中からインデックスを入れ替えるような
計算量の多いタスクを削減することができる。
最後に格納したデータから順に取り出す→スタック
スタックにデータを格納するのをプッシュ、取り出すことはポップと呼ばれる

まずはスタックとキューを実装→使い方を確認する
"""
#スタックの挙動を実際に調べてみる
stack = []
stack.append(3)
stack.append(5)
stack.append(2)
print(stack)

temp = stack.pop()
print(temp)
temp =stack.pop()
print(temp)

#値をポップした後のスタックはどうなっているか？
print(stack)


#キューの挙動を実際に調べてみる
import queue

q = queue.Queue()
q.put(3)
q.put(5)
q.put(2)
print(q)

temp = q.get()
print(temp)
temp = q.get()
print(temp)

q.put(4)

temp =q.get()
print(temp)

"""
ヒープは木構造のデータ構造で、子ノードの値は親ノードと比べ等しいか大きくなる、という条件を設ける。
ヒープに要素を追加する場合、木構造の最後の部分に要素を追加する。
ヒープを使って値をソートするには、追加した要素と親ノードを比較し親ノードの方が小さければそれと
交換する、というタスクを繰り返す。
ヒープを使ったソートの計算数はO(n・logn)となる。これはn個のノードがある木の高さがlog2(n)であり、
計算数が2の対数に比例する為である。選択ソートと比べると、処理速度が格段に向上する。
"""
data = [6,15,4,2,8,5,11,9,7,13]
data = [1,2,3,4,5,6,7,8,9,10]
calcurated = 0

print("データのリスト：")
print(data)

#ヒープ構造を構成する
for i in range(len(data)):
    j = i
    #子ノードが親ノードよりも小さいかを判定
    while (j>0) and (data[(j-1)//2] < data[j]):
        #あてはまる場合は、親ノードと交換する
        data[(j-1)//2] , data[j] = data[j], data[(j-1)//2]
        #交換が終わったら、親ノードの探索に移行する
        j = (j-1)//2

        calcurated +=1
print("ヒープ構造構成後：")
print(data)

#ヒープ構造になったリストをソートする
for i in range(len(data), 0, -1):
    #ヒープの先頭と交換
    data[i-1], data[0] = data[0], data[i-1]
    j = 0
    #親ノードの左下・右下の値の方が小さい場合
    while ((2*j+1 < i-1) and (data[j] < data[2*j+1])) or ((2*j+2 < i-1) and (data[j] < data[2*j+2])):
        #左下>右下の場合
        if(2*j+2 == i-1) or (data[2*j+1] > data[2*j+2]):
            #親ノードと交換
            data[j], data[2*j+1] = data[2*j+1], data[j]
            #探索するノードを左下に移動
            j = 2*j+1
            calcurated +=1
        #右下>左下の場合
        else:
            #親ノードと交換
            data[j], data[2*j+2] = data[2*j+2], data[j]
            #探索するノードを右下に移動
            j = 2*j+2
            calcurated +=1

#ソートを実行する
print("ソート後：")
print(data)
print("処理回数：")
print(calcurated)

"""
マージソート - ソートしたいデータを2分割するタスクを繰り返し、これらがバラバラになった状態から
ソートを開始する。n個リストを分割した際の段数はlog2(n)となり、リストが結合されるまでの計算時間はヒープソートと同様
O(n・logn)となる。
"""
data = [6,15,4,2,8,5,11,9,7,13]

print("データのリスト：")
print(data)

#マージソートを実行する為の関数
def merge_sort(data):
    #データが1つしかない→値をそのまま返す
    if len(data) <= 1:
        return data
    #リストの中央のインデックスを計算
    mid = len(data)//2
    #データの右側
    left=merge_sort(data[:mid])
    #データの右側
    right=merge_sort(data[mid:])
    #データを結合する
    return merge(left, right)

#データ結合を実行するための関数
def merge(left, right):
    result = []
    i,j = 0,0

    while (i<len(left)) and (j<len(right)):
        #左<＝右の時 - 返り値に左側のリストから取り出して追加
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        #右<＝左の時 - 返り値に右側のリストから取り出して追加
        else:
            result.append(right[j])
            j += 1

    #残りをまとめて追加する
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

print("ソート後：")
print(merge_sort(data))


"""
クイックソート - リストからデータを1つ選び、小さい要素と大きい要素に分割する。
分割の基準となる値はピボット(Pivot)という。
このタスクを再帰的に繰り返し、データ数が1になるまで繰り返す
"""
data = [6,15,4,2,8,5,11,9,7,13]

print("データのリスト：")
print(data)

#マージソートを実行する為の関数
def quick_sort(data):
    #データ数が1になるまで繰り返す
    if len(data) <= 1:
        return data

    #ピボットの値はデータの先頭とする
    pivot = data[0]
    left, right, same = [], [], 0

    for i in data:
        #値がピボットより小さい→左側のリストにアペンド
        if i < pivot:
            left.append(i)
        #値がピボットより大きい→右側のリストにアペンド
        elif i > pivot:
            right.append(i)
        else:
            same += 1
        #左側を再帰的にクイックソート
        left = quick_sort(left)
        #右側を再帰的にクイックソート
        right = quick_sort(right)

        #ソートされた値 + ピボットと一致した値
        return left + [pivot]*same + right

print("ソート後：")
print(quick_sort(data))

"""
ソートアルゴリズムは、たいていPythonのsortメソッドを使うと最も高速な処理を
自動で行ってくれる。詳しくは書籍の表を引用する予定
"""
