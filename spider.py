# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 10:11
# @Author : 张思惠
# @File : spider.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import re
import urllib.request
import sqlite3
import xlwt
def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getdata(baseurl)



def getdata(url):
    datalist=[]
    for i in range(0,10):
        html=askurl(url+str(i*25))
    return datalist


def askurl(url):
    head={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 100.0.4896.60Safari / 537.36Edg / 100.0.1185.29"
    }
    requestt=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(requestt)
        html=response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

if __name__=="__main__":
    main()