#猫眼总榜电影类型抓取
import csv
import requests
import time
from bs4 import BeautifulSoup
import lxml
import re
import json

pattern = r"\d+"
myheader = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    }

def __init__(url):
    time.sleep(1)
    rsps = requests.get(url, headers = myheader)
    if rsps.status_code == 200:
        return rsps.text
    else:
        print("False")

def movielist(rsps):
    soup = BeautifulSoup(rsps, 'lxml')
    with open(f'类型数据.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['电影名称', '电影类型'])
        for i in soup.select('#ranks-list > .row'):
            num = i['data-com']
            skipnum = re.findall(pattern, num)[0]
            skipurl = f'https://piaofang.maoyan.com/movie/{skipnum}'
            newrsps = __init__(skipurl)
            #time.sleep(1)
            newsoup = BeautifulSoup(newrsps, 'lxml')
            #print(newsoup)
            sections = newsoup.find('div', class_ = 'sections')
            #print(sections)
            movie_container = sections.find('div', class_ = 'movie-container')
            info_detail = movie_container.find('div', class_ = 'info-detail')
            info_detail_title = info_detail.find('div', class_ = 'info-detail-title')
            moviename = info_detail_title.find('span', class_ = 'info-title-content').text
            info_detail_extra = info_detail.find('div', class_ = 'info-detail-extra')
            movietype = info_detail_extra.find('p', class_ = 'info-category').text
            writer.writerow([moviename, movietype])
            print(moviename)
            print(movietype)



url = f"https://piaofang.maoyan.com/rankings/year"
real_rsps = __init__(url)
moviedetail = movielist(real_rsps)
