# coding: UTF-8

import sys
import numpy as np
from wave_io import read
from wave_io import save


########## 専門実験C3に直接関係するところ：ここから ##########

# 信号 x と信号 y を足し合わせる関数
def add_wave(x, y):

    Lx = len(x) # 信号 x の長さを変数 Lx に格納
    Ly = len(y) # 信号 y の長さを変数 Ly に格納
    if Lx != Ly:
        # x と y の長さが一致しない場合はエラー狩猟
        print("エラー: add_wave(): 信号 x と信号 y の長さが一致しません．")
        return np.empty(0)

    # 【TODO】長さ Lx の一次元配列 z を作成



    # 【TODO】x と y を要素ごとに足し合わせ，その結果を配列 z の各要素に格納



    # 配列 z を戻値として返却
    return z

########## 専門実験C3に直接関係するところ：ここまで ##########


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 4:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python combine.py [入力ファイル1] [入力ファイル2] ... [出力ファイル]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したファイル名を変数に格納
    input_filenames = [] # 入力ファイル名リスト（文字列の配列）
    for i in range(1, len(sys.argv) - 1):
        input_filenames.append(sys.argv[i])
    output_filename = sys.argv[len(sys.argv) - 1] # 出力ファイル名（文字列型）


    ########## 専門実験C3に直接関係するところ：ここから ##########

    # 入力ファイルの個数を変数 K に格納
    K = len(input_filenames)

    # 最初の入力ファイルから音声信号を読み出し，一次元配列 x に格納
    x = read(input_filenames[0])

    # 二番目以降の入力ファイルから音声信号を読み出し，順次足し合わせる
    for i in range(1, K):
        y = read(input_filenames[i]) # 次の入力ファイルから音声信号を読み出し，一次元配列 y に格納
        x = add_wave(x, y) # x と y を足し合わせ，その結果を x に格納（13行目で定義した関数 add_wave を呼び出す）

    # 足し合わせた結果を出力信号としてファイルに保存
    save(x, output_filename)

    ########## 専門実験C3に直接関係するところ：ここまで ##########


    exit(0)
