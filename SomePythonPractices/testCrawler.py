# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:46:19 2019

@author: Jarry
"""
# Try to build a crawler
#Using requests
#Learned from seizeeveryday
import requests
import pandas as pd
import numpy as np
import json
import time
import random
import os
from lxml import etree
import socket
"""
The original page is movie.douban.com
By checking the page we found the only thing changed was the 'start=0'
Each time it add 20
The data format is json
"""
url1 = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0'
url2 = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20'
url3 = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40'
url4 = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=60'

#Build the pages
def format_url(num):
    urls = []
    base_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}'
    for i in range(0,20 * num,20):
        url = base_url.format(i)
        urls.append(url)
    return urls

urls = format_url(5)

#Simulate a header 
#A great library which called fake-useragent can simulate different agent
# pip install fake-useragent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

#Process retrived page information
def parse_base_info(url,headers):
    
    html = requests.get(url,headers = headers)   
    bs = json.loads(html.text)
    
    df = pd.DataFrame()
    
    for i in bs['data']:
        title = i['title']  #片名
        casts = i['casts']  #主演
        cover = i['cover']  #海报
        directors = i['directors']  #导演
        m_id = i['id']  #ID
        rate = i['rate'] #评分
        star = i['star'] #标记人数 
        url = i['url']  #网址
        cache = pd.DataFrame({'Casts':[casts],'Cover':[cover],'Directors':[directors],
                              'ID':[m_id],'Rates':[rate],'Stars':[star],'Title':[title],'URL':[url]})
        df = pd.concat([df,cache]) #form a new dataframe
    return df

#iteratively obtain the results
result = pd.DataFrame()

count = 1
for url in urls:
    df = parse_base_info(url,headers = headers)
    result = pd.concat([result,df])
    time.sleep(random.random() + 2)
    print('I had crawled page of:%d' % count)
    count += 1

#result.head()

#-----------------------------------------------------------------
"""
Obtain information for each movie
"""
def parse_movie_info(url,headers = headers,ip = ''):
    if ip == '':
        html = requests.get(url,headers = headers)
    else:
        html = requests.get(url,headers = headers,proxies = ip)
    bs = etree.HTML(html.text)
    # xpath is used to locate the position of XML
    # We can copy Xpath using web browser
    title = bs.xpath('//div[@id = "wrapper"]/div/h1/span')[0].text  

    year = bs.xpath('//div[@id = "wrapper"]/div/h1/span')[1].text   

    m_type = []
    for t in bs.xpath('//span[@property = "v:genre"]'):
        m_type.append(t.text)   
    a = bs.xpath('//div[@id= "info"]')[0].xpath('string()')

    m_time =a[a.find('片长: ') + 4:a.find('分钟\n')]  #时长

    area = a[a.find('制片国家/地区:') + 9:a.find('\n        语言')]  #地区

    try:
        people = bs.xpath('//a[@class = "rating_people"]/span')[0].text
    #评分分布
        rating = {}
        rate_count = bs.xpath('//div[@class = "ratings-on-weight"]/div')
        for rate in rate_count:
            rating[rate.xpath('span/@title')[0]] = rate.xpath('span[@class = "rating_per"]')[0].text
    except:
        people = 'None'
        rating = {}
    #简介
    try:
        brief = bs.xpath('//span[@property = "v:summary"]')[0].text.strip('\n                                \u3000\u3000')
    except:
        brief = 'None'
    
    try:
        hot_comment = bs.xpath('//div[@id = "hot-comments"]/div/div/p/span')[0].text
    except:
        hot_comment = 'None'
    cache = pd.DataFrame({'片名':[title],'上映时间':[year],'电影类型':[m_type],'片长':[m_time],
                          '地区':[area],'评分人数':[people],'评分分布':[rating],'简介':[brief],'热评':[hot_comment],'网址':[url]})
    return cache


#IP = socket.gethostbyname(socket.gethostname())

movie_result = pd.DataFrame()
ip = ''  #IP pool
count2 = 1
cw = 1

for url,name in zip(result['URL'].values,result['Title'].values):
#for name,url in wrongs.items():
    try:
        cache = parse_movie_info(url,headers = headers,ip = ip)
        movie_result = pd.concat([movie_result,cache])
        #time.sleep(random.random())
        print('我们爬取了第:%d部电影-------%s' % (count2,name))
        count2 += 1
    except:
        print('滴滴滴滴滴，第{}次报错'.format(cw))
        print('ip is:{}'.format(ip))
        cw += 1
        time.sleep(2)
        continue

movie_result.to_excel('MovieResult.xlsx')