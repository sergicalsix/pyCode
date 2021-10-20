# Pandas を高速化するには
## apply関数を使う
並列化できるライブラリを使う

https://blog.ikedaosushi.com/entry/2020/07/26/173109


## dataframe -> vaex
Vaexは，Pandasに似たOut-of-Core DataFramesを用いて，大規模な表形式のデータセットを視覚化し，探索するためのpythonライブラリです。平均、合計、数、標準偏差などの統計量を、N次元グリッド上で毎秒10億個（）のオブジェクト/行まで計算できます。また、ヒストグラム、密度プロット、3Dボリュームレンダリングを用いて可視化し、ビッグデータのインタラクティブな探索を可能にします。Vaexは、メモリマッピング、ゼロメモリコピーポリシー、遅延計算を使用して、最高のパフォーマンス（メモリを無駄にしない）を実現しています。

- 機械学習
https://blog.ikedaosushi.com/entry/2019/04/14/173307
-  包括的
https://qiita.com/simonritchie/items/13b6c1b73d0635a0b54f

parqetに直して処理できる

- github
https://github.com/vaexio/vaex

## dataframe -> cuDF