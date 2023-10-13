from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
new_movie=[]

data=pd.read_excel(io='test.xlsx')
data_df=pd.DataFrame(data)
new_data=pd.read_excel(io='new_data.xlsx')
new_data_df=pd.DataFrame(new_data)
data_list1=[]
data_list2=[]
new_data_list=[]
new_data_result=[]
for i in range(len(new_data)):
    data=[new_data.iloc[i]['a'],new_data.iloc[i]['d'],new_data.iloc[i]['e']]#将一个电影的所有特征值作业放到一个列表中作为xi
    #a=地区 b=场次 c=人次
    new_data_list.append(data)#将xi插入到特征值列表中


#print(new_data_list) 
for i in range(31):
    data_=[data_df.loc[i,'a'],data_df.loc[i,'d'],data_df.loc[i,'e']]#a=地区 b=场次 c=人次
    data_list1.append(data_)
    data_list2.append(data_df.loc[i,'c'])


new_box=[]
def BoxOffice(List_1,List_2,new_list):
    #电影特征值 List1  票房List2
    #new_list 新的预测票房的特征值列表
    model=LinearRegression()
    model.fit(List_1,List_2)
    
    for i in new_list:

        prediction=model.predict(np.array(i).reshape(1,-1))
        new_box.append(prediction)

# 在机器学习时，对随机值进行处理后可能会输出负值
#而在发生复制的情况是场次大于人次


BoxOffice(data_list1,data_list2,new_data_list)
for i in new_box:
    new_data_result.append(i[0])

#print(data_df)
#print(new_data_df)
#print(new_data_result)

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
predlist_city=['江苏','四川','天津','辽宁','内蒙古','重庆']
list_pred=[]
for i in new_data_result:
    list_pred.append(i)


listdata_pred = [round(x, 2) for x in list_pred]



c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(predlist_city, listdata_pred)],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2023下半年\n部分城市票房预测占比图"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: \n{c}"))
    .render('232.html')
)
