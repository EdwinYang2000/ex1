#!/usr/local/anaconda3/bin/python3

import json
import pandas as pd
import matplotlib.pyplot as plt

#代码必须写入 ~/Code/datafigure.py 文件中；
#代码执行方法是 /home/shiyanlou/anaconda3/bin/python datafigure.py，执行后将绘制并显示图片
#注意 y 轴的数据是该用户所有学习记录中 minutes 这一项的 sum()
#线型图标题为 StudyData，Y 轴标签为 Study Time，X 轴标签为 User ID
#优化考虑：x 轴的用户 ID 可以考虑使用 ID 范围
#数据图的类型为线型图，图的 X 轴为用户 ID，Y 轴为用户总学习时间。


#def analysis(file, user_id):
    # times = 0
    #minutes = 0
    #df = pd.read_json(file)
    # times ==int(user_id)].shape[0]
    #minutes = df[df['user_id'] == int(user_id)]['minutes'].sum()

    #return minutes


file = 'user_study.json'

df = pd.read_json(file)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.set_title('StudyData')

x = df['user_id']

sum_list = []

for i in x:
    sum_list.append(df[df['user_id'] == i]['minutes'].sum())


ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')


ax.plot(x, sum_list,'b-')

fig.show()


