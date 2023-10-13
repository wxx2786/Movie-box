#豆瓣Top250电影评论抓取
import requests
import json
from bs4 import BeautifulSoup
import random
import xlsxwriter

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
]

def getHeaders():
    i = random.randint(0, 10)
    user_agent = user_agents[i]
    headers = {
        'User-Agent': user_agent
    }
    return headers

def gennerateIds():
    ids=[]
    infos=[]
    url = 'https://movie.douban.com/j/new_search_subjects?sort=R&range=0,10&tags=电影&countries=中国大陆&year_range=2020,2020'
    for i in range(10):
        params={"start":20*i}
        response = requests.get(url, headers=getHeaders(),params=params)
        data = json.loads(response.text)
        datalist = data["data"]
        for item in datalist:
            ids.append(item["id"])
            infos.append((item["id"],item["title"],item["rate"],item["casts"],item["directors"]))
    return ids,infos

def pauseComment(commenthtml):
    id=commenthtml['data-cid']
    name=commenthtml.div.a['title']
    span=commenthtml.find_all('span',attrs={"class":"short"})[0]
    text=span.text
    return id,name,text


if __name__ == '__main__':
    ids,infos=gennerateIds()

    workbook = xlsxwriter.Workbook('data3.xlsx')
    worksheet = workbook.add_worksheet('comments')
    worksheet1 =workbook.add_worksheet('movie_info')

    # 写入 Movieinfos
    rowindex=1
    for info in infos:
        mid=info[0]
        title=info[1]
        rate=info[2]
        casts=""
        dires=""
        for name in info[3]:
            casts+=name+" "
        for name in info[4]:
            dires+=name+" "
        worksheet1.write_row(rowindex,0,(mid,title,rate,casts,dires))
        rowindex+=1

    # 写入影评数据
    rowindex=1
    for id in ids:
        print(id)
        commenturl="https://movie.douban.com/subject/"+id+"/comments?status=P"
        response2 = requests.get(commenturl, headers=getHeaders())
        html = BeautifulSoup(response2.text, 'xml')
        comments = html.find_all("div", attrs={"class": "comment-item "})
        for comment in comments:
            cid,name,text=pauseComment(comment)
            worksheet.write_row(rowindex, 0, (id,cid,name,text))
            rowindex+=1

    workbook.close()
