# coding: UTF-8

import sys
import numpy as np
from math import pi
from math import cos
from wave_io import save


########## 専門実験C3に直接関係するところ：ここから ##########

# 単一周波数の正弦波を生成する関数
#   A: 振幅（0.0 ～ 1.0）
#   f: 周波数（0 ～ 4000）
#   theta: 初期位相（-π ～ π）
#   N: 信号の長さ（生成するサンプルの数）・・・ 本実験では 8000点 で固定とする
#   fs: サンプリング周波数 ・・・ 本実験では 8000[Hz] で固定とする
def make_sinwave(f, A, theta, N=8000, fs=8000):

    # 【TODO】長さ N の一次元配列 x を作成



    # 【TODO】配列 x の各要素に信号値をセット



    # 配列 x を戻値として返却
    return x

########## 専門実験C3に直接関係するところ：ここまで ##########


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 5:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python sinwave.py [周波数] [振幅] [初期位相] [出力ファイル名]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したパラメータ値やファイル名を変数に格納
    f = np.float32(sys.argv[1]) # 周波数（float型，0 ～ 4000）
    A = np.float32(sys.argv[2]) # 振幅（float型，0.0 ～ 1.0）
    theta = np.float32(sys.argv[3]) # 初期位相（float型，-π ～ π）
    output_filename = sys.argv[4] # 出力ファイル名（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 正弦波を生成し，一次元配列 x に格納
    x = make_sinwave(f, A, theta) # 18行目で定義した関数 make_sinwave を呼び出す

    # 出力信号 x をファイルに保存
    save(x, output_filename)

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    exit(0)
