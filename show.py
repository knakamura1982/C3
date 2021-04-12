# coding: UTF-8

import sys
import numpy as np
import matplotlib.pyplot as plt
from wave_io import read


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 2:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python show.py [入力ファイル名]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したファイル名を変数に格納
    input_filename = sys.argv[1] # 入力ファイル名（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 入力ファイルから音声信号を読み出し，一次元配列 x に格納
    x = read(input_filename)

    # 入力信号 x の長さを変数 Lx に格納
    Lx = len(x)

    # 入力信号 x のサンプル値を標準出力に表示
    for n in range(0, Lx): # for ループ（C言語の for (int n = 0; n < Lx; ++n) と同じ意味）
        print("x[{0}] = {1}".format(n, x[n])) # n 番目のサンプル値 x[n] を出力

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    # 入力信号 x の波形をグラフで表示
    print("")
    print("グラフを閉じるとプログラムが終了します．")
    t = np.arange(0, Lx)
    plt.figure(figsize=(12, 4))
    # plt.xlim(0, 8000) # 横軸の範囲を 0 ～ 8000 に設定（必要に応じてアンコメントし，自由に変更して下さい）
    # plt.ylim(-0.6, 0.6) # 縦軸の範囲を -0.6 ～ 0.6 に設定（必要に応じてアンコメントし，自由に変更して下さい）
    plt.plot(t, x)
    plt.show()

    exit(0)
