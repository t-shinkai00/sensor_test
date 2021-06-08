import requests
from variables import TOKEN,CHANNEL
files = {'file': open("/root/sensor_test/images/2021-06-09 03:09:05.292639.jpg", 'rb')}  #****に送付ファイル名記載。絶対パスで記載が安全。 

param = {
     'token':"36WPIHl1lubZlABuyRyGdb3F",
     'channels':"C024DRUKXGS",
    #  'filename':"DLファイル名",　 #.txtとかファイル名を付ける
     'initial_comment': "動きを検知しました。",
     'title': "様子"
 }

requests.post(
     'https://slack.com/api/files.upload', 
     params=param, 
     files=files,
)