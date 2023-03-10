"""
アルゴリズムを実務で役立てるため、最短経路問題を解けるアルゴリズムを実装してみる
カーナビで最短・最速のルートを表示する、ネットワークを効率よく繋ぐ、
マネジメントで必要な作業を真っ先に終わらせクリティカルパスをなるべく短くするなど
最短経路問題はさまざまな課題解決に応用できる。
"""
"""
頂点がn個ある無向グラフの場合、とある頂点から別の頂点に移動するまでの組み合わせのパターン数はn!通りとなる。
このパターン数を出来るだけ削減するか、より良いアルゴリズムで近似的に解く方法を考える
"""
"""
ベルマン・フォード法
グラフの辺の値に注目し、頂点を移動するのに必要な「重み」を考える
重みの値は初期値は暫定的に正の無限大とする
計算を進めるにつれて重みを更新することで最短経路の長さの暫定値が更新されていき、
最終的には最後の頂点までの最短経路が算出できる

頂点数をn、辺の数をmとすると、ベルマン・フォード法の計算量はO(n*m)となる
"""
def bellman_ford(edges, num_v):
    dist = [float("inf") for i in range(num_v)]
    dist[0] = 0
    changed = True

    #重みが更新されなくなるまで繰り返し
    while changed:
        for edge in edges:
            #起点と終点の間の重みを更新する
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True
    return dist

#頂点間を結ぶ辺の重みのリスト[起点、終点、重み]
edges = [
[0,1,4],[0,2,3],[1,2,1],[1,3,1],
[0,4,5],[2,5,2],[4,6,2],[5,4,1],
[5,6,4]
]

print(bellman_ford(edges, 7))

"""
ダイクストラ法
辺の重みではなく頂点と頂点の間でコストがもっとも小さくなるものを選択する、頂点の「重み」に注目した探索法
ダイクストラ法では選択する頂点を工夫することでベルマン・フォード法よりも計算量を削減することができる
"""
def dijkstra(edges, num_v):
    dist = [float("inf") for i in range(num_v)]
    dist[0] = 0
    q = [i for i in range(num_v)]

    #頂点の数だけ、最もコストが小さくなる頂点の組み合わせを探索する
    while len(q) > 0:
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i
        u = q.pop(q.index(r))
        for i in edges[u]:
            #より短い重みの経路があれば、それを更新する
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
    return dist

#辺の重みのリスト[頂点[終点、重み]]
edges = [
[[1,4],[2,3]], #頂点A
[[2,1],[3,1],[4,5]], #頂点B
[[5,2]], #頂点C
[[4,3]], #頂点D
[[6,2]], #頂点E
[[4,1],[6,4]], #頂点F
[] #頂点G
]

print(dijkstra(edges, 7))

"""
リストを使った処理について実力が付いた
今後は機械学習や統計・データ分析に力を入れ、特に基礎的な線形代数や微積分・情報工学の基礎を学びたい
実際にデータをレポートにしたり、マーケティングやピープルアナリティクスに応用して自動化・労働生産性の向上を目指す
"""
