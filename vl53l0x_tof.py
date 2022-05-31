#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time             #time(sleepを使うためのモジュール)のインポート
import VL53L0X          #VL53L0X(spi通信を行うためのモジュール)のインポート

"""メイン関数"""
if __name__ == '__main__':
    """VL53L0Xのインスタンスを作成"""
    tof = VL53L0X.VL53L0X(address=0x29)

    #距離の取得を開始する
    tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    try:
        while True:
            dist = tof.get_distance()/float(10)   #VL53L0Xから距離[cm]を取得する
            print ("%0.1f cm " % dist)     #距離[cm]を表示する
            time.sleep(1)               #1[s]スリープする
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))                   #例外処理の内容をコンソールに表示
    finally:
        tof.stop_ranging()              #VL53L0Xの終了処理
        print("\nexit program")         #プログラムが終了することを表示する