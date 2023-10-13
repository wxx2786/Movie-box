import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.charts import EffectScatter
from pyecharts.charts import Pie
from pyecharts.charts import Line
import matplotlib.pyplot as plt  # 在任何绘图之前，我们需要一个figure对象，可以理解成我们需要一张画板才能开始绘图
import jieba  # jieba库是中文分词的第三方库（中文文本需要通过分词获得单个的词语）
from wordcloud import WordCloud  # 导入wordcloud库
 
df1=pd.read_csv(r'排行榜数据.csv')
allpri=df1['票房（万元）']
filname=df1['电影名称']
top_filname=filname[:5]
top_filname=list(top_filname)
top_allpri=allpri[:5]
top_allpri=list(top_allpri)


c = (
    Bar()
    .add_xaxis(top_filname)
    .add_yaxis('票房数据',top_allpri)
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="2018-2022总票房top5"))
)
c.render('2018-2022总票房top5.html')    #2018-2022总票房top5


df2=pd.read_csv(r'排行榜数据_2018.csv')
pri_18=df2['票房（万元）']
pri_18=list(pri_18[:10])
film_18=df2['电影名称']
film_18=list(film_18[:10])


c = (
    EffectScatter()
    .add_xaxis(film_18)
    .add_yaxis("票房数据",pri_18)
    .set_global_opts(title_opts=opts.TitleOpts(title="2018-top10电影票房"),
                     xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":25}))
        )
c.render('2018-top10电影票房.html')    #2018-top10电影票房





x_data =film_18
y_data =pri_18
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        series_name="电影票房",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="2018-top10电影票房占比（单位：万元）",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
).render('2018-top10电影票房占比.html')        #2018-top10电影票房占比



df2['month'] = df2['上映时间'].map(lambda r:r.split('-')[1])
df2.drop(axis = 1, columns = '电影名称',inplace=True)
df1['month'] = df1['上映时间'].map(lambda r:r.split('-')[1])
df1.drop(axis = 1, columns = '电影名称',inplace=True)
df1.groupby('month')['票房（万元）'].sum()
pri_total=df1.groupby('month')['票房（万元）'].sum().to_numpy()
pri_total=pri_total.tolist()
month_list=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']



c = (
    Pie()
    .add(
        " 票房占比",
        [list(z) for z in zip(month_list,pri_total)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="\n2011-2023\n每月票房占比统计"))
)
c.render('2011-2023每月票房占比统计.html')      #2011-2023每月票房占比统计


total_18=df2['票房（万元）'].sum()
  #2018电影总票房
df3=pd.read_csv(r'排行榜数据_2019.csv')
total_19=df3['票房（万元）'].sum()
total_19     #2019电影总票房
df4=pd.read_csv(r'排行榜数据_2020.csv')
total_20=df4['票房（万元）'].sum()
total_20     #2020电影总票房
df5=pd.read_csv(r'排行榜数据_2021.csv')
total_21=df5['票房（万元）'].sum()
total_21     #2021电影总票房
df6=pd.read_csv(r'排行榜数据_2022.csv')
total_22=df6['票房（万元）'].sum()
total_22     #2022电影总票房
year_list=['2018','2019','2020','2021','2022']
total_list=tests=[6048440, 6388695, 1985520, 4680509, 2990912]



x_data = year_list
y_data = total_list

(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="票房总量",
        y_axis=y_data,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2018-2022历年票房总和", subtitle=""),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        xaxis_opts=opts.AxisOpts(boundary_gap=False),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} W"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            dimension=0,
            pieces=[
                {"lte": 2020, "color": "green"},
                {"gt": 2020, "lte": 2022, "color": "red"}
            ],
        ),
    )

).render('2018-2022历年票房总和.html')    #2018-2022历年票房总和


df2.head(1)['票房（万元）'].to_numpy().tolist()
df3.head(1)['票房（万元）'].to_numpy().tolist()
df4.head(1)['票房（万元）'].to_numpy().tolist()
df5.head(1)['票房（万元）'].to_numpy().tolist()
df6.head(1)['票房（万元）'].to_numpy().tolist()
df2.head(10)
tp = (round(df2.head(10)['票房（万元）'].mean()/10000,2),round(df3.head(10)['票房（万元）'].mean()/10000,2),round(df4.head(10)['票房（万元）'].mean()/10000,2),round(df5.head(10)['票房（万元）'].mean()/10000,2),round(df6.head(10)['票房（万元）'].mean()/10000,2))
list_ =[]

for i in tp:
    round(i,2)
    list_.append(i)


anver_peo=list((df2.head(10)['观影人数'].mean(),df3.head(10)['观影人数'].mean(),df4.head(10)['观影人数'].mean(),df5.head(10)['观影人数'].mean(),df6.head(10)['观影人数'].mean()))




c = (
    Bar()
    .add_xaxis(list(range(2018,2023)))
    .add_yaxis("top-10平均票房（单位：亿元）",list_)
    .add_yaxis("top-10平均观影人次", anver_peo)
    .set_global_opts(title_opts=opts.TitleOpts(title="2018-2022\ntop10票房与平均观影人次", subtitle=""))
)
c.render_notebook()     #2018-2022top10票房与平均观影人次

provence_data=pd.read_excel(r'各省数据.xlsx')


ppppte=['广东省', '江苏省', '浙江省', '四川省', '上海市', '北京市', '山东省', '湖北省', '河南省', '福建省', '安徽省', '湖南省', '河北省', '辽宁省', '陕西省', '江西省', '重庆市', '广西壮族自治区', '山西省', '云南省', '天津市', '黑龙江省', '内蒙古自治区', '吉林省', '贵州省', '甘肃省', '新疆维吾尔自治区', '海南省', '宁夏回族自治区', '青海省', '西藏自治区']
pro_sell=provence_data['票房(万元)']
sell_list=pro_sell.to_list()
list23=[]
for i in sell_list:
    list23.append(i)
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("票房（单位：万元）", [list(z) for z in zip(ppppte, list23)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2023各省市票房总和"),
        visualmap_opts=opts.VisualMapOpts(max_=50000, is_piecewise=True),
    )
)
c.render('2023各省市票房总和.html')     




text = open(r'leixing.txt','r',encoding='utf-8').read()  # 读入txt文本数据，在字符串前面加上字符r或R之后表示原始字符串，字符串中的任意字符都不再进行转义，后一个r表示“只读”
cut_text = jieba.cut(text)  # 结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
result = " ".join(cut_text)  # 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
# join函数的用法：'sep'.join(seq)参数说明：sep：分隔符。可以为空；seq：要连接的元素序列、字符串、元组、字典；即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
 
# 生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
wc = WordCloud(font_path='C:\Windows\Fonts\msyhbd.ttc',background_color='white',max_font_size=150)
wc.generate(result) # 根据分词后的文本产生词云
wc.to_file(r"wordcloud.png")  # 保存绘制好的词云图
plt.imshow(wc)  # 以图片的形式显示词云
plt.axis("off")  # 关闭图像坐标系，即不显示坐标系
plt.show()  # plt.imshow()函数负责对图像进行处理，并显示其格式，但是不能显示。其后必须有plt.show()才能显示