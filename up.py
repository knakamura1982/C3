# coding: UTF-8

import sys
import numpy as np
from wave_io import read
from wave_io import save


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 3:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python up.py [入力ファイル] [出力ファイル]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したファイル名を変数に格納
    input_filename = sys.argv[1] # 入力ファイル名（文字列型）
    output_filename = sys.argv[2] # 出力ファイル名（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 入力ファイルから音声信号を読み出し，一次元配列 x に格納
    x = read(input_filename)

    # 入力信号 x の長さを変数 Lx に格納
    Lx = len(x)

    # 【TODO】出力信号の長さ Ly を適切に定めたのち，
    #         Ly 個分のサンプルを格納する一次元配列 y を作成



    # 【TODO】アップサンプリングの処理を実行



    # 出力信号 y を出力ファイルに保存
    save(y, output_filename)

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    exit(0)
