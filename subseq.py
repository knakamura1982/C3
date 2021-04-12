# coding: UTF-8

import sys
import numpy as np
from wave_io import read
from wave_io import save


# エントリポイント： C言語で言うところの main 関数
if __name__ == "__main__":

    if len(sys.argv) < 4:
        # コマンドライン引数が足りないときは実行方法を表示
        print("実行方法： python subseq.py [入力ファイル名] [指定区間の開始位置] [指定区間の長さ] [出力ファイル名]", file=sys.stderr)
        exit(1)

    # コマンドライン引数で指定したパラメータ値やファイル名を変数に格納
    input_filename = sys.argv[1] # 入力ファイル名（文字列型）
    output_filename = sys.argv[4] # 出力ファイル名（文字列型）
    s = int(sys.argv[2]) # 指定区間の開始位置（整数型）
    l = int(sys.argv[3]) # 指定区間の長さ（整数型）

    # 入力ファイルから音声信号を読み出し，一次元配列 x に格納
    x = read(input_filename)

    # 入力信号 x の長さを変数 Lx に格納
    Lx = len(x)

    # 指定区間が入力信号の範囲内に収まっているかどうかをチェック
    e = s + l # 指定区間の終了位置（e の一つ手前まで）
    if s < 0 or Lx < e:
        print("エラー: 指定区間 [{0}, {1}] は入力信号（長さ {2}）の範囲内に収まっていません．".format(s, e-1, Lx), file=sys.stderr)
        exit(1)
    if l <= 0:
        print("エラー: 指定区間の長さとして 0 以下の値が指定されています．".format(s, e-1, Lx), file=sys.stderr)
        exit(1)

    # 指定区間を抜き出す
    y = x[s : e] # 配列 x から x[s] ～ x[e-1] を抜き出して新たな配列 y とする（「スライス」という）
    y[0] = 1.0 if y[0] < 0 else -1.0 # 処理結果を分かりやすくするため，先頭の値 y[0] は 1 または -1 に強制変更する

    # 抜き出した指定区間を出力ファイルに保存
    save(y, output_filename)

    exit(0)
