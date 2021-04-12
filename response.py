# coding: UTF-8

import sys
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from fourier_io import read_fourier_coeff


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 3:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python response.py [入力信号のフーリエ係数ファイル] [出力信号のフーリエ係数ファイル]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したファイル名を変数に格納
    filename_a = sys.argv[1] # 入力信号のフーリエ係数ファイルの名前（文字列型）
    filename_b = sys.argv[2] # 出力信号のフーリエ係数ファイルの名前（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 入力信号のフーリエ係数データを読み込む（絶対値：abs_a，偏角：arg_a）
    abs_a, arg_a = read_fourier_coeff(filename_a)

    # 出力信号のフーリエ係数データを読み込む（絶対値：abs_b，偏角：arg_b）
    abs_b, arg_b = read_fourier_coeff(filename_b)

    # 二つのフーリエ係数データのサイズが一致しているか否かをチェック
    if len(abs_a) != len(abs_b):
        print("エラー: 入力信号と出力信号でフーリエ係数データのサイズが一致しません．", file=sys.stderr)
        exit(1)

    # フーリエ係数データのサイズ（配列長）を変数 M に格納
    M = len(abs_a)

    # 【TODO】振幅スペクトルの比および位相スペクトルの差を格納する一次元配列 abs_H, arg_H を用意（長さ M ）



    # 【TODO】振幅特性，すなわち振幅スペクトルの比を求める（分母が 0 となる場合に注意）



    # 【TODO】位相特性，すなわち位相スペクトルの差を求める（結果が -π ～ π の範囲に収まるようにすること）



    ########## 専門実験C3に直接関係するところ：ここまで ##########


    # 振幅特性（amplitude response）と位相特性（phase response）をグラフで表示
    print("")
    print("グラフを閉じるとプログラムが終了します．")
    t = np.arange(0, M)
    plt.figure(figsize=(6, 8))
    plt.subplot(2, 1, 1)
    plt.title('[Top] amplitude response, [Bottom] phase response')
    plt.ylim(0, 1.2) # 振幅特性（上側のグラフ）における縦軸の範囲を 0 ～ 1.2 に設定（必要に応じて変更して構いません）
    plt.plot(t, abs_H)
    plt.subplot(2, 1, 2)
    plt.ylim(-3.3, 3.3) # 位相特性（下側のグラフ）における縦軸の範囲を -3.3 ～ 3.3 に設定（必要に応じて変更して構いません）
    plt.plot(t, arg_H)
    plt.show()

    exit(0)
