#coding:gbk
from requests import get
from json import loads
from urllib.parse import quote
s=input("请输入始发站：")
e=input("请输入终到站：")
d=input("请输入时间（YYYY-MM-DD）：")
s=quote(s)
e=quote(e)
d=quote(d)
url="https://train.qunar.com/dict/open/s2s.do?&dptStation=%s&arrStation=%s&date=%s&user=neibu"%(
    s,e,d
)
json=loads(get(url=url).text)
# print(json)
if(json["errcode"] != 0 or json["data"]["s2sBeanList"] == []):
    print("查不到！")
    __import__("sys").exit(0)
json=json["data"]["s2sBeanList"]
for j in json:
    print("-"*100)
    i=j["extraBeanMap"]
    print("车次：%s"%j["trainNo"])
    print("本列车始发站：%s"%j["startStationName"])
    print("本列车终点站：%s"%j["endStationName"])
    print("上车站名：%s"%j["dptStationName"])
    print("下车站名：%s" % j["arrStationName"])
    print("开车时间：%s"%j["dptTime"])
    print("下车时间：%s" % j["arrTime"])
    print("开售时间：%s"%i["startSaleTime"])
    print("列车类型：%s"%i["trainType"])
    print("全程：%s"%i["interval"])
    print("票务信息：")
    # print(i)


