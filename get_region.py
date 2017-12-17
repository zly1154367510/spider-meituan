#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from bs4 import BeautifulSoup as bfl
import requests
import random_headers as rh
import toCsv
import time
import urllib2
import chardet
'''
'''
url = "http://www.meituan.com/changecity/"

def open_html_content(url):
    random_headers = rh.get_random_headers()
    headers = {'User-Agent': random_headers}
    request = urllib2.Request(url=url,headers=headers)
    response = urllib2.urlopen(request)
    return response



def get_region_list(url):
    urlList = []
    nameList = []
    content = open_html_content(url)
    soup = bfl(content,"html.parser")
    regionUrlList = soup.select(".cities > a")
    for i in regionUrlList:
        urlList.append(i.get("href"))
        nameList.append(i.text)
    data = [(u,n) for u,n in zip(urlList,nameList)]
    return data


def get_category(url,name):
    time.sleep(1)
    urlList = []
    nameList = []
    try:
        content = open_html_content(url)
    except:
        print "错误"
        return
    soup = bfl(content,"html.parser")
    category = soup.select(".detail-area > .detail-content > a")
    for i in category[0:28]:
        urlList.append(i.get("href"))
        nameList.append(name)
    data = [(u, n) for u, n in zip(urlList, nameList)]
    return data

def get_business_msg(url):
    item_info = []#d单个商家信息
    items = []#所有商家信息
    try:
       print "i"
    except:
        print "没有捕捉到商家信息"
        return
    content = requests.get(url).text
    print content
    # soup = bfl(content, "html.parser")
    # business_msg = soup.select(".info > h4")
    # for i in business_msg:
    #     print i







if __name__ == '__main__':
    urlList = toCsv.read_csv("re1")
    for i in urlList['0']:
        get_business_msg(i)
