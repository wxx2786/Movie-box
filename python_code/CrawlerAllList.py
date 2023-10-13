#18~23年猫眼年度排行抓取
import requests
from bs4 import BeautifulSoup
import time
import csv

data={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}
for year in range(2018, 2024):
    url = f"https://piaofang.maoyan.com/rankings/year?year={year}&limit=100&tab={2024 - year}"

    with open(f'{year}数据.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['电影名称', '上映时间', '票房（万元）', '平均票价', '观影人数'])

        res=requests.get(url,headers=data)
        time.sleep(2)

        soup=BeautifulSoup(res.text,'lxml')
        res2=soup.find('div',id="ranks-list")
        list_res2=res2.find_all('ul',class_="row")
        for list in list_res2:
            moviename = list.find('p',class_="first-line").text
            uptime = list.find('p',class_="second-line").text
            boxOffice = list.find('li',class_="col2 tr").text
            aver_price = list.find('li',class_="col3 tr").text
            num_p = list.find('li',class_="col4 tr").text
            writer.writerow([moviename, uptime, boxOffice, aver_price, num_p])