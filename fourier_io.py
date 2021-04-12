# coding: UTF-8

import csv
import numpy as np
from numpy.fft import fft


# 複素数の実部を取得する関数
def Re(z):
    return z.real


# 複素数の虚部を取得する関数
def Im(z):
    return z.imag


# 信号 x をフーリエ級数展開したときのフーリエ係数を求める関数
def fourier(x):

    # FFTを行う（ライブラリを使用）
    a = fft(x)

    # FFTの結果を 1/N 倍して離散時間フーリエ級数展開の定義に合わせる
    a = a / a.shape[0]

    return a


# CSVファイルからフーリエ係数の絶対値と偏角を読み出す関数
def read_fourier_coeff(filename):

    # ファイルを開く
    f = open(filename, 'r')
    reader = csv.reader(f)

    # フーリエ係数の絶対値と偏角を読み出す
    abs = []
    arg = []
    for row in reader:
        abs.append(float(row[1]))
        arg.append(float(row[2]))
    abs = np.asarray(abs)
    arg = np.asarray(arg)

    # ファイルを閉じる
    f.close()

    return abs, arg


# フーリエ係数の絶対値と偏角をCSV形式でファイルに保存する関数
# 0 番目 ～ N 番目の係数のみを保存する
def save_fourier_coeff(filename, abs, arg, N=-1):

    # 保存範囲が指定されていない場合，強制的に N=(配列長)/2 とする
    if N < 0:
        N = min(abs.shape[0], arg.shape[0])
        N = (N // 2) + 1

    # ファイルを開く
    f = open(filename, 'w')

    # フーリエ係数の絶対値と偏角を保存
    for k in range(0, N):
        f.write('{0}[Hz],{1},{2}\n'.format(k, abs[k], arg[k]))

    # ファイルを閉じる
    f.close()
