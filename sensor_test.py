#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import picamera
import slackweb
import subprocess
import time
from time import sleep
from fluent import sender
logger = sender.FluentSender('sensor', host = '127.0.0.1', port = 24224)
import requests

# 距離を読む関数
def read_distance():
    # 必要なライブラリのインポート・設定
    import RPi.GPIO as GPIO

    # 使用するピンの設定
    GPIO.setmode(GPIO.BOARD)
    TRIG = 11 # ボード上の11番ピン(GPIO17)
    ECHO = 13 # ボード上の13番ピン(GPIO27)

    # ピンのモードをそれぞれ出力用と入力用に設定
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, GPIO.LOW)

    # TRIG に短いパルスを送る
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # ECHO ピンがHIGHになるのを待つ
    signaloff = time.time()
    while GPIO.input(ECHO) == GPIO.LOW:
        signaloff = time.time()

    # ECHO ピンがLOWになるのを待つ
    signalon = signaloff
    while time.time() < signaloff + 0.1:
        if GPIO.input(ECHO) == GPIO.LOW:
            signalon = time.time()
            break

    # GPIO を初期化しておく
    GPIO.cleanup()

    # 時刻の差から、物体までの往復の時間を求め、距離を計算する
    timepassed = signalon - signaloff
    distance = timepassed * 17000

    # 500cm 以上の場合はノイズと判断する
    if distance <= 500:
        return distance
    else:
        return None

# import os
# import datetime
# from datetime import gspread
# from linebot import LineBotApi
# from linebot.models import TextSendMessage
from variables import TOKEN,CHANNEL

while True:
    start_time = time.time()
    distance = read_distance()

    # # https://docs.google.com/spreadsheets/d/xxxx/edit#gid=0 の xxxx の部分を環境変数で指定
    # spreadsheet_id = os.getenv('1S0rUZIxFyaZAddBeZspdOYvE-lPrYwmY4mFk6pXNXfg')
    # gc = gspread.service_account()
    # sh = gc.open_by_key(spreadsheet_id)
    # sheet = sh.sheet1
    # values = sheet.get_all_records()
    # # ヘッダー行 + 既存レコードの行数の次の行に書き込む
    # sheet.update(f'A{len(values) + 2}:C',[[str(datetime.now()), distance, image]])

    # channel_access_token = os.getenv('WwO7kJ0tJquIvmlGb1vaxOGqD66WyassanTrW/RMoMUGGxK7c4eevtpMbfBuMzSG0E7/NB7xThbbhk+Is8XZ4TTJPoF1vsY5ouv1+N7uY49+VQU0/kzb43dT7kVlfUFU5mQrK07ekIg2DRcveTUd3AdB04t89/1O/w1cDnyilFU=')
    # line_user_ids = os.getenv('4b36e2b79617c6dc3a19f24d2aa9e6e2').split(',')
    # line_bot_api = LineBotApi(channel_access_token)

    if distance:
        print("距離: %.1f cm" % (distance))
        ret_dict = {
            'mean_dis': distance,
        }
        logger.emit('distance', ret_dict)
        if distance>50:
            print('動きを感知しました。')
            camera = picamera.PiCamera()
            dt_now = datetime.datetime.now()
            camera.close()
            subprocess.run(['raspistill','-o','/root/sensor_test/images/'+str(dt_now)+'.jpg'])

            files = {'file': open('/root/sensor_test/images/'+str(dt_now)+'.jpg', 'rb')}
            param = {
                'token':TOKEN,
                'channels':CHANNEL,
                #  'filename':"DLファイル名",　 #.txtとかファイル名を付ける
                'initial_comment': "動きを検知しました。",
                'title': str(dt_now)+'.jpg',
            }

            requests.post(
                'https://slack.com/api/files.upload', 
                params=param, 
                files=files,
            )
            break

    # １秒間に１回実行するためのウェイトを入れる
    wait = start_time + 1 - start_time
    if wait > 0:
        time.sleep(wait)
