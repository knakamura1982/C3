# coding: UTF-8

import numpy as np


# 単一周波数の正弦波を生成する関数
#   A: 振幅（0.0 ～ 1.0）
#   f: 周波数（0 ～ 4000）
#   theta: 初期位相（-π ～ π）
#   N: 信号の長さ（生成するサンプルの数）・・・ 本実験では 8000点 で固定とする
#   fs: サンプリング周波数 ・・・ 本実験では 8000[Hz] で固定とする
def make_sinwave(f, A, theta, N=8000, fs=8000):
    t = np.arange(0, N)
    return A * np.cos((2 * np.pi * f / fs) * t + theta)


# 信号 x と信号 y を足し合わせる関数
def add_wave(x, y):
    return x + y
