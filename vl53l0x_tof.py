#!/usr/bin/env python
#-*- coding utf-8 -*-

import time
import VL53L0X

if __name__ == '__main__':
    
    #VL530Xのインスタンス生成
    tof = VL53L0X.VL53L0X(address=0x29)

    #距離の取得を開始する
    tof.start_ranging(VL53L0X.VL530X_BETTER_ACCURACY_MODE)

    try:
        while True:
            #距離[cm]を取得する
            dist = tof.distance()/float(10)
            #距離[cm]の表示
            print('%0.1f cm' % dist)
            time.sleep(1)               #1[s]スリープする
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))                   #例外処理の内容をコンソールに表示
    finally:
        tof.stop_ranging()              #VL53L0Xの終了処理
        print("\nexit program")         #プログラムが終了することを表示する