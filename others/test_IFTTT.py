import requests
 
# IFTTT_Webhook
def ifttt_webhook(eventid,key):
    payload = {"value1": "https://qiita.com/?scope=weekly", "value2": "Of", "value3": "Things" }
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + key
    response = requests.post(url, data=payload)
 
# ここからスタート
if __name__ == '__main__':
    print ("IFTTT連携開始")
    event_name = "test"
    key = "mF_AD_ppM1D1jMm1LRwTeaybO00BWddPTfcixC43XNU"   
    # IFTTT_Webhook
    ifttt_webhook(event_name, key)
 
    print ("IFTTT連携終了")
