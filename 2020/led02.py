# L チカ 10 回

# 必要なモジュールを宣言
import RPi.GPIO as GPIO # GPIO を利用する
import time             # sleep を利用する

PNO = 4   # 対象の GPIO ポート番号

# GPIO の初期化
GPIO.setmode(GPIO.BCM)    # BCM モード（ポート番号で指定する方法）
GPIO.setup(PNO, GPIO.OUT) # 指定した番号を out に設定

# 10 回繰り返す
for i in range(10):
    print("i=", i)
    GPIO.output(PNO, GPIO.HIGH)
    #GPIO.output(PNO, True)
    time.sleep(0.3)
    GPIO.output(PNO, GPIO.LOW)
    #GPIO.output(PNO, False)
    time.sleep(0.3)

GPIO.cleanup()

