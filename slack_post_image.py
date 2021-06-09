import requests
from variables import TOKEN,CHANNEL
files = {'file': open("/root/sensor_test/images/2021-6-9-3-4.jpg", 'rb')}  #****に送付ファイル名記載。絶対パスで記載が安全。 

param = {
     'token':TOKEN,
     'channels':CHANNEL,
    #  'filename':"DLファイル名",　 #.txtとかファイル名を付ける
     'initial_comment': "動きを検知しました。",
     'title': "/root/sensor_test/images/2021-6-9-3-4.jpg"
 }

requests.post(
     'https://slack.com/api/files.upload', 
     params=param, 
     files=files,
)