from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
arr_list1=[]
bofc_list1=[]
person_list1=[]
person_list2=[]
person_data_list=[]
person_data_result=[]
new_box=[]
def read(textname):
    dr=pd.read_csv(textname)
    df=pd.DataFrame(dr)
   
    for i in range(len(df)):
        arr_list1.append([df.iloc[i]['平均票价'],df.iloc[i]['观影人数']])
        bofc_list1.append(df.iloc[i]['票房（万元）'])


for i in range(2018,2023,1):
    read(f'排行榜数据-{i}.csv')        

new_data=[]
new_data_result=[]
dr_1=pd.read_csv('排行榜数据-year.csv')
df_1=pd.DataFrame(dr_1)
for i in range(len(df_1)):
    new_data.append([df_1.iloc[i]['平均票价'],df_1.iloc[i]['观影人数']])

new_box=[]
def BoxOffice(List_1,List_2,new_list):
    #电影特征值 List1  票房List2
    model=LinearRegression()
    model.fit(List_1,List_2)
    
    for i in new_list:

        prediction=model.predict(np.array(i).reshape(1,-1))
        new_box.append(prediction)

# 在机器学习时，对随机值进行处理后可能会输出负值
#而在发生复制的情况是场次大于人次

BoxOffice(data_list1,data_list2,new_data)
for i in new_box:
    new_data_result.append(i[0])


#print(df_1)
#print(new_data_result)

toptic_pre=new_data_result[10:20]
pertic_list = [round(x, 2) for x in toptic_pre]
#print(pertic_list)
ticpre=pd.read_csv(r'排行榜数据-year.csv')
tic_datatop=ticpre.iloc[10:20]
tic_data=tic_datatop['票房（万元）'].tolist()
filna_datatop=ticpre.iloc[10:20]
filna_data=filna_datatop['电影名称'].tolist()

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(filna_data)
    .add_yaxis("当前票房", tic_data)
    .add_yaxis("预测票房", pertic_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="2023下半年票房预测", subtitle=""))
    .render('233.html')
)