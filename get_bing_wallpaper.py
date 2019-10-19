#!/usr/bin/python3
# coding:utf-8
# date 2019.10.19
# author : dashazi

from faker import Faker
import requests
from bs4 import BeautifulSoup
import time


year = time.localtime()[0]
month = time.localtime()[1]
day = time.localtime()[2]
filename = '{}_{}_{}.jpg'.format(year,month,day)

url = 'https://cn.bing.com/'

f = Faker()
useragent = f.user_agent()
a = requests.get(url,headers = {'user-agent':useragent})
if a.status_code == 200:
    b = BeautifulSoup(a.text,'lxml')
    pic_url = b.select('link')[0]['href']
    print('[FOUND!] url:{}'.format(url+pic_url))
    pic_rsp = requests.get(url+pic_url,headers={'user-agent':useragent})

    with open(filename,'wb') as f:
        for i in pic_rsp:
            f.write(i)

