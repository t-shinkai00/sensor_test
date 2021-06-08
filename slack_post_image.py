import requests

TOKEN = 'xoxb-166105950720-2155928837204-NZWMyJBhjO5ggIBemEVrfycS' #上記に取得方法記載してます
CHANNEL = 'C024DRUKXGS' #上記に取得方法記載してます 
files = {'file': open("/root/sensor/images/2021-6-9-2-32.jpg", 'rb')}  #****に送付ファイル名記載。絶対パスで記載が安全。 

param = {
     'token':"xoxb-166105950720-2155928837204-NZWMyJBhjO5ggIBemEVrfycS",
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