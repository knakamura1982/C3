# coding: UTF-8

import sys
import csv
import numpy as np
from wave_io import save
from fourier_io import read_fourier_coeff
from func import make_sinwave # sinwave.py で設計した関数 make_sinwave を使う
from func import add_wave # combine.py で設計した関数 add_wave を使う


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 4:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python reconstruct.py [入力ファイル名] [f_max] [出力ファイル名]", file=sys.stderr)
        print("  f_max: 正弦波を足し合わせる際の上限周波数（0[Hz] から f_max[Hz] までを足し合わせる）", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したパラメータ値やファイル名を変数に格納
    input_filename = sys.argv[1] # 入力ファイル名（文字列型）
    output_filename = sys.argv[3] # 出力ファイル名（文字列型）
    f_max = int(sys.argv[2]) # 正弦波を足し合わせる際の上限周波数（整数型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 入力ファイルからフーリエ係数の絶対値および偏角を読み出し，一次元配列 abs, arg に格納
    abs, arg = read_fourier_coeff(input_filename)

    # 【TODO】直流成分（0[Hz] の正弦波）を生成して一次元配列 x に格納する
    #         フーリエ係数に基づいて適切な振幅・初期位相を設定すること



    # 【TODO】1[Hz] から f_max[Hz] の正弦波を順次生成し，足し合わせる
    #         フーリエ係数に基づいて適切な振幅・初期位相を設定すること



    # 足し合わせた結果を出力信号としてファイルに保存
    save(x, output_filename)

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    exit(0)
