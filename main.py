#coding:gbk
from requests import get
from json import loads
from urllib.parse import quote
s=input("������ʼ��վ��")
e=input("�������յ�վ��")
d=input("������ʱ�䣨YYYY-MM-DD����")
s=quote(s)
e=quote(e)
d=quote(d)
url="https://train.qunar.com/dict/open/s2s.do?&dptStation=%s&arrStation=%s&date=%s&user=neibu"%(
    s,e,d
)
json=loads(get(url=url).text)
# print(json)
if(json["errcode"] != 0 or json["data"]["s2sBeanList"] == []):
    print("�鲻����")
    __import__("sys").exit(0)
json=json["data"]["s2sBeanList"]
for j in json:
    print("-"*100)
    i=j["extraBeanMap"]
    print("���Σ�%s"%j["trainNo"])
    print("���г�ʼ��վ��%s"%j["startStationName"])
    print("���г��յ�վ��%s"%j["endStationName"])
    print("�ϳ�վ����%s"%j["dptStationName"])
    print("�³�վ����%s" % j["arrStationName"])
    print("����ʱ�䣺%s"%j["dptTime"])
    print("�³�ʱ�䣺%s" % j["arrTime"])
    print("����ʱ�䣺%s"%i["startSaleTime"])
    print("�г����ͣ�%s"%i["trainType"])
    print("ȫ�̣�%s"%i["interval"])
    print("Ʊ����Ϣ��")
    # print(i)


