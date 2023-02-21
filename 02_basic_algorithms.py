"""
倍数・商と余りの判定、素数やフィボナッチ数など、四則演算を使った基礎的なアルゴリズム

FizzBuzz
3の倍数に対してFizz、5の倍数に対してBuzz、15の倍数に対してFuzzBuzzと出力する
#論理的に排他的となるものの優先度を高めに設定する
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

"""
おつりの計算
おつりの金額が紙幣・硬貨に換算するとそれぞれ何枚になるかを計算する
金額の高い通貨から商・余りを計算するアルゴリズムを1円になるまで繰り返す
アルゴリズムを実装する際は、データ型が合っているか、おつり額がマイナスでないかというフェイルセーフ・前提条件のチェックを行う。
"""
import sys

input_price = 100
product_price = 120
change = input_price - product_price

#フェイルセーフ開始-------------------
if change < 0:
    print("おつり額が不足しています：")
    sys.exit()

#フェイルセーフ完了-------------------

coin = [5000,1000,500,100,50,10,5,1]

for i in coin:
    #金額の高い通貨から商(枚数)・余り(次の通貨への繰り越し)を
    #計算するアルゴリズムを1円になるまで繰り返す
    r = change // i
    change %= i
    print("通貨額:" + str(i) + " | 枚数:" + str(r) + " | 残り金額:" + str(change) )

"""
10進数→2進数への変換をするアルゴリズム
10進数→2進数への変換を行うには、元の数を2で割り商と余りを求める→商をさらに2で割り、余りの数を桁に足すというルーチンを繰り返す
"""
n = 1000
result=""

while n > 0:
    result = str(n%2) + result
    n //=2

print(result)

"""
割る数を変えるだけで、基数から10進数への変換をするアルゴリズム全般が実装できる
"""
n = 1000

def convert(n, base):
    result=""
    while n > 0:
        result = str(n%base) + result
        n //=base

    return result

print(convert(n, 8))

"""
2進数→10進数への変換をするアルゴリズム
2進数→10進数への変換を行うには対応する桁の累乗部分の変換を繰り返し、その値の総和を求める
"""
n = "101010111"
result=0

for i in range(len(n)):
    result += int(n[i])* (2**(len(n)-i-1))

print(result)

"""
整数が素数かを判定するアルゴリズム
整数が素数化は、その整数の平方根以下の整数が約数となるかを調べる。
なぜ平方根以下かは帰無法で証明できるので、様参照。
"""
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(100):
    if isPrime(i):
        print(i, end=" | ")

"""
整数が素数かを判定するアルゴリズム:エラトステネスの篩
素数を判定する際、判定済みの数の倍数となる数を除外することで素数計算の効率を高める
"""
import math

def getPrime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    data = [i +1 for i in range(2,n,2)]
    while limit > data[0]:
        prime.append(data[0])
        #割り切れなかった値のみ追加
        data = [j for j in data if j % data[0] != 0]
    return prime + data

print(getPrime(100000))

"""
SymPyを使うと、素数を使ったアルゴリズムが簡潔に書ける
"""
pip install sympy
from sympy import sieve

primes = [i for i in sieve.primerange(0, 1000)]
print(primes)

"""
フィボナッチ数列を求めるアルゴリズム
再帰的に漸化式を計算し、フィボナッチ数列のような値を求める
"""
def fibonacci(n):
    if (n==1)or(n==2):
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

for i in range(1, 30):
    print(str(fibonacci(i)) + " | ")

"""
フィボナッチ数列を求めるアルゴリズムを改良：
すでに算出した値をコレクションに加え、無駄な計算を削減する。この手法は「メモ化」と呼ばれる
"""
#数列のメモ化には辞書型を用いる
fibonacci_dict = {1:1, 2:1}

def fibonacci(n):
    #フィボナッチ数列の辞書にその値があれば、その値を返す
    #新しくフィボナッチ数を求めたら、その値を辞書に追加しておく
    if n in fibonacci_dict:
        return fibonacci_dict[n]

    fibonacci_dict[n] = fibonacci(n-2) + fibonacci(n-1)
    return fibonacci_dict[n]

for i in range(1, 30):
    print(str(fibonacci(i)) + " | ")
