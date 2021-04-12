# coding: UTF-8

import wave
import array
import numpy as np


# 32-bit float を 16-bit int に変換する際の倍率
SCALE_FACTOR = 32767


# ファイルから音声信号を読み出す関数
#   filename: 入力ファイル名
#   返値: モノラル音声を表現する一次元配列（numpy 配列）
def read(filename, C3mode=True):
    w = wave.open(filename, 'r')
    nc = w.getnchannels() # チャンネル数を読み出す
    sw = w.getsampwidth() # サンプルあたりのバイト数を読み出す
    fs = w.getframerate() # サンプリング周波数を読み出す
    data = w.readframes(w.getnframes()) # 音声データを読み出す
    y = np.frombuffer(data, dtype=np.int16)
    x = y.astype(np.float32) / SCALE_FACTOR
    if C3mode == True:
        if nc != 1:
            print("エラー: {0}: モノラル音声ではありません．".format(filename))
        if sw != 2:
            print("エラー: {0}: サンプルあたりのバイト数が 2 ではありません．".format(filename))
        if fs != 8000:
            print("警告: {0}: サンプリング周波数が 8000[Hz] ではありません．".format(filename))
        w.close()
        return x
    else:
        w.close()
        return x, fs


# 音声信号をファイルに保存する関数
#   x: 音声データ
#   filename: 出力ファイル名
#   fs: サンプリング周波数（本実験では 8000[Hz] で固定）
#   返値: なし
def save(x, filename, fs=8000):
    x = SCALE_FACTOR * x
    b = array.array('h', x.astype(np.int16)).tobytes()
    w = wave.Wave_write(filename)
    w.setnchannels(1) # チャンネル数を出力： 本実験では 1（モノラル）で固定
    w.setsampwidth(2) # サンプルあたりのバイト数を出力： 本実験では 2 バイトで固定
    w.setframerate(fs) # サンプリング周波数を出力
    w.writeframes(b) # 音声データを出力
    w.close()
