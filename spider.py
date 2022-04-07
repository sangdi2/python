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
    savepath="豆瓣电影top250.xls"
    savedb="movie.db"
    savedatadb(datalist,savedb)
    # savedata(datalist,savepath)


findlink=re.compile(r'<a href="(.*?)">')
findimgsrc=re.compile(r'<img.*src="(.*?)"',re.S)
findtitle=re.compile(r'<span class="title">(.*)</span>')
findrating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findjudge=re.compile(r'<span>(\d*)人评价</span>')
findinq=re.compile(r'<span class="inq">(.*)</span>')
findbd=re.compile(r'<p class="">(.*?)</p>',re.S)


def getdata(url):
    datalist=[]
    for i in range(0,10):
        html=askurl(url+str(i*25))
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            data=[]
            item=str(item)

            link=re.findall(findlink,item)[0]
            print(link)
            data.append(link)

            imgsrc=re.findall(findimgsrc,item)[0]
            data.append(imgsrc)

            title=re.findall(findtitle,item)
            if len(title)==2:
                data.append(title[0])
                data.append(title[1].replace("/",""))
            else:
                data.append(title[0])
                data.append(" ")

            rating=re.findall(findrating,item)[0]
            data.append(rating)

            judge=re.findall(findjudge,item)[0]
            data.append(judge)

            inq=re.findall(findinq,item)
            if len(inq)!=0:
                data.append(inq[0].replace("。",""))
            else:
                data.append(" ")

            bd=re.findall(findbd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd=re.sub('/'," ",bd)
            data.append(bd.strip())

            datalist.append(data)

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


def savedata(datalist,savepath):
    workbook=xlwt.Workbook(encoding="utf-8",style_compression=True)
    sheet=workbook.add_sheet("sheet1",cell_overwrite_ok=True)
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    workbook.save(savepath)


def savedatadb(datalist,savedb):
    init_db(savedb)
    conn=sqlite3.connect(savedb)
    cur=conn.cursor()
    for item in datalist:
        for index in range(len(item)):
            if index==4 or index==5:
                continue
            item[index]='"'+item[index]+'"'
        sql='''
            insert into movie(
            info_link,pic_link,cname,ename,score,rated,instroduction,info
            )values (%s)
        '''%",".join(item)
        cur.execute(sql)
        conn.commit()
    cur.execute(sql)
    conn.close()




def init_db(savedb):
     sql='''
     create table movie
     (
     id integer primary key autoincrement,
     info_link text,
     pic_link text,
     cname varchar,
     ename varchar,
     score numeric,
     rated numeric,
     instroduction text,
     info text
     )
     '''
     conn =sqlite3.connect(savedb)
     cursour =conn.cursor()
     cursour.execute(sql)
     conn.commit()
     conn.close()


if __name__=="__main__":
    main()