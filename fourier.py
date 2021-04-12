# coding: UTF-8

import sys
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import atan2
from wave_io import read
from fourier_io import Re
from fourier_io import Im
from fourier_io import fourier
from fourier_io import save_fourier_coeff


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 3:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python fourier.py [入力ファイル名] [出力ファイル名]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したファイル名を変数に格納
    input_filename = sys.argv[1] # 入力ファイル名（文字列型）
    output_filename = sys.argv[2] # 出力ファイル名（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # ファイルから音声信号を読み出し，一次元配列 x に格納
    x = read(input_filename)

    # 入力信号 x の長さを変数 N に格納
    N = len(x)

    # 入力信号 x をフーリエ級数展開したときのフーリエ係数を求める
    a = fourier(x) # フーリエ係数の列（複素数の配列，長さ N ）

    # 【TODO】フーリエ係数の絶対値および偏角を格納するの一次元配列 abs, arg を確保する（長さ N ）



    # 【TODO】フーリエ係数の絶対値および偏角を求める（ただし絶対値が 0.00001 より小さい場合は偏角は 0 とみなす）
    #         複素数 z の実部は Re(z)，虚部は Im(z) で求められる
    #         実数 X の平方根は関数 sqrt(X) で，tan^{-1}(Y/X) は atan2(Y,X) で計算できる



    # abs と arg をファイルに保存
    save_fourier_coeff(output_filename, abs, arg)

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    # フーリエ係数の絶対値と偏角をグラフで表示
    # なお，これらを一般に振幅スペクトル（amplitude spectrum）および位相スペクトル（phase spectrum）と呼ぶ
    print("")
    print("グラフを閉じるとプログラムが終了します．")
    M = (N // 2) + 1 # 表示範囲はナイキスト周波数までとする
    t = np.arange(0, M)
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    plt.title('[Top] amplitude spectrum, [Bottom] phase spectrum')
    plt.plot(t, abs[0 : M])
    plt.subplot(2, 1, 2)
    plt.plot(t, arg[0 : M])
    plt.show()

    exit(0)
