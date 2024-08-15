1 import requests
2 import json
3 import re
4 headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
5 def qq_video(url):
6 appver = '3.2.19.333'
7 try:
8 vid = url.split('/')[-1].split('.')[0]
9 except:
10 vid = url
11 #print(vid)
12 url = 'http://vv.video.qq.com/getinfo?otype=json&platform=11&defnpayver=1&appver=' + appver + '&defn=fhd&vid=' + vid
13 html = requests.get(url,headers = headers)
14 html_text = html.text
15 #print(html.text)
16 jsonstr = re.findall('QZOutputJson=(.+);/pre>,html_text,re.S)[0]
17 #print(jsonstr)
18 json_data = json.loads(jsonstr)
19 fvkey = json_data['vl']['vi'][0]['fvkey']
20 keyid = json_data['vl']['vi'][0]['cl']['ci'][0]['keyid'].split(".")
21 filename = keyid[0] + ".p" + keyid[1][2:] + "." + keyid[2] + ".mp4"
22 cdn = json_data['vl']['vi'][0]['ul']['ui'][3]['url']
23 downloadurl = cdn + filename + "?vkey=" + fvkey + "?type=mp4"
24 print("DownloadUrl:" + downloadurl)
25 if __name__ == "__main__":
26 url = input("Put:")
27 qq_video(url)


