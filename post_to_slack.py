#coding: UTF-8

import slackweb
import requests

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
attachments = []
attachment = {
    "title": "動きを感知しました。",
    "text": "ここにテキスト。",
}
attachments.append(attachment)
# slack.notify(attachments=attachments)

files = {'file': open("images/2021-6-9-2-32.jpg", 'rb')}
param = {'token':'xoxb-166105950720-2155928837204-NZWMyJBhjO5ggIBemEVrfycS', 'channels':"T4W33TYM6","title": "動きを感知しました。",}
res = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
# import requests
# import json
# import pandas as pd
# import numpy as np
# import matplotlib

# matplotlib.use('Agg') # CUI環境でmatplotlib使いたい場合、指定する
# import matplotlib.pyplot as plt

# TOKEN = # 取得したトークン
# CHANNEL = T4W33TYM6

# #####################################
# # 画像を生成する例、アップロードするだけなら不要
# #####################################

# # データ読み込む
# data = pd.read_table(
#     "/path/to/data/input.tsv", #なんかtsv/csv読み込むサンプル
#     header=-1, 
#     names=("date","value")
# )
# # 軸の基準になるとこ
# data.index = pd.to_datetime(data.iloc[:,0])
# data.plot()
# # 保存するよ
# plt.savefig('figure.png')

# ###############
# # 画像送信ここから
# ###############
# files = {'file': open("figure.png", 'rb')}
# param = {
#     'token':TOKEN, 
#     'channels':CHANNEL,
#     'filename':"filename",
#     'initial_comment': "initial_comment",
#     'title': "title"
# }
# requests.post(url="https://slack.com/api/files.upload",params=param, files=files)