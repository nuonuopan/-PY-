
#%%从tushare并保存本地获取数据
import tushare as ts
ts_pro=ts.pro_api()
ts_code='000001.SZ'
start_date='20180101'
end_date='20191230'
df=ts_pro.daily(ts_code=ts_code,start_date=start_date,end_date=end_date)
df=df.reindex(index=df.index[::-1])
used_cols=['trade_date','close']
df=df[used_cols]
df.to_csv(r'F:\assert\《Py量化金融》\data\{0}_{1}_{2}.csv'.format(ts_code,start_date,end_date),index=False)


#%%
#MA10 和 MA20 双均线策略
#%%
import pandas as pd
import numpy as np
import ffn


#从本地导入数据
df=pd.read_csv(r'F:\assert\《Py量化金融》\data\000001.SZ_20180101_20191230.csv')


#初始化全局变量
#是否持仓
hold=False
#持仓数
pos=0
#回测资金
capital=100000
#剩余资金
rest=0
#手续费万分之三
fee=0.0003
#每日资金数列表
capital_list=[]
#20日均线数组
MA20_array=np.zeros(20)
#10日均线数组
MA10_array=np.zeros(10)
#交易次数
count=0
# #记录交易盈亏
# profit_loss=[]
# 计算每日的MA10 和MA20，并且每条数据都进行开仓、平仓判断
# 遍历每一条历史数据
for i in range(len(df)):
    #k用来标记时候进行了运算
    k=0
    #最新数据
    price=df['close'][i]
    date=df['trade_date'][i]
    #数据平移
    MA10_array[0:9]=MA10_array[1:10]
    MA20_array[0:19]=MA20_array[1:20]
    #新数据添加到数据组末尾
    MA10_array[-1]=price
    MA20_array[-1]=price
    #for循环小于20下面的语句不会执行
    if i<20:
        continue
    MA10=MA10_array.mean()
    MA20=MA20_array.mean()
    #判断是否达到开平仓信号
    #开仓
    if MA10>MA20 and hold==False:
        #计算开仓数目
        pos=int(capital/price/100)*100
        #计算剩余资金
        rest=capital-pos*price*(1+fee)
        #持仓设置为True
        hold=True
        print('buy at',date,'price',price,'capital',capital)
        count=count+1
        print(count)
        # k=1
    #平仓
    elif MA10<MA20 and hold==True:
        #计算平仓后的资金
        capital=pos*price*(1-fee)+rest
        #持仓数归0
        pos=0
        #持仓状态设置为False
        hold=False
        print('buy at',date,'price',price,'capital',capital)
        count=count+1
        print(count)
        # k=1
    #计算每日的资金数目
    if hold==True:
        capital_list.append(rest+pos*price)
    else:
        capital_list.append(capital)
    
    # #计算每次交易的盈亏
    # if k==1

#计算回测结果
#每日资金数目变series
capital_series=pd.Series(capital_list)
#资金序列的简单收益序列
capital_return=capital_series.shift(1)-capital_series
#资金序列的简单收益率序列
capital_returns=ffn.to_returns(capital_series)

#计算策略收益率 大好  策略结束时总共的收益率
print('策略收益率：\n',round(ffn.calc_total_return(capital_series),4)*100,'%')
#计算最大回撤 小好
print('最大回撤:\n',round(ffn.calc_max_drawdown(capital_series),4)*100,'%')
#计算夏普比率 大好
print('夏普比率：\n',round(ffn.calc_sharpe(capital_returns),4)*100,'%')
#计算索提诺比率（策略亏损的风险） 大好
print('索提诺比率：\n',round(ffn.calc_sortino_ratio(capital_returns),4)*100,'%')
#可视化资金曲线
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ["SimHei"]    # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False 
fig=plt.figure()
fig.add_subplot(111)
plt.plot(capital_list,color='r')
plt.title('双均线策略的资金曲线')
plt.show()


#%%
#RSI6策略
#%%
import pandas as pd
import numpy as np
import ffn
import talib

df=pd.read_csv(r'F:\assert\《Py量化金融》\data\000001.SZ_20180101_20191230.csv')


#初始化全局变量
#是否持仓
hold=False
#持仓数
pos=0
#回测资金
capital=100000
#剩余资金
rest=0
#手续费万分之三
fee=0.0003
#每日资金数列表
capital_list=[]
#用于计算RSI6指标的数组
RSI6_array=np.zeros(7)
#交易次数
count=0
# #记录交易盈亏
# profit_loss=[]
# 计算每日的MA10 和MA20，并且每条数据都进行开仓、平仓判断
# 遍历每一条历史数据
for i in range(len(df)):
    #k用来标记时候进行了运算
    k=0
    #最新数据
    price=df['close'][i]
    date=df['trade_date'][i]
    #数据平移
    RSI6_array[0:6]=RSI6_array[1:7]
    #新数据添加到数据组末尾
    RSI6_array[-1]=price
    #for循环小于20下面的语句不会执行
    if i<6:
        continue
    rsi6=talib.RSI(RSI6_array,timeperiod=6)[-1]
    #判断是否达到开平仓信号
    #开仓
    if rsi6<=20 and hold==False:
        #计算开仓数目
        pos=int(capital/price/100)*100
        #计算剩余资金
        rest=capital-pos*price*(1+fee)
        #持仓设置为True
        hold=True
        print('buy at',date,'price',price,'capital',capital)
        count=count+1
        print(count)
        # k=1
    #平仓
    elif rsi6>=80 and hold==True:
        #计算平仓后的资金
        capital=pos*price*(1-fee)+rest
        #持仓数归0
        pos=0
        #持仓状态设置为False
        hold=False
        print('buy at',date,'price',price,'capital',capital)
        count=count+1
        print(count)
        # k=1
    #计算每日的资金数目
    if hold==True:
        capital_list.append(rest+pos*price)
    else:
        capital_list.append(capital)
    
    # #计算每次交易的盈亏
    # if k==1

#计算回测结果
#每日资金数目变series
capital_series=pd.Series(capital_list)
#资金序列的简单收益序列
capital_return=capital_series.shift(1)-capital_series
#资金序列的简单收益率序列
capital_returns=ffn.to_returns(capital_series)

#计算策略收益率 大好  策略结束时总共的收益率
print('策略收益率：\n',round(ffn.calc_total_return(capital_series),4)*100,'%')
#计算最大回撤 小好
print('最大回撤:\n',round(ffn.calc_max_drawdown(capital_series),4)*100,'%')
#计算夏普比率 大好
print('夏普比率：\n',round(ffn.calc_sharpe(capital_returns),4)*100,'%')
#计算索提诺比率（策略亏损的风险） 大好
print('索提诺比率：\n',round(ffn.calc_sortino_ratio(capital_returns),4)*100,'%')

# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ["SimHei"]    # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False 
# fig=plt.figure()
# fig.add_subplot(111)
# plt.plot(capital_list,color='r')
# plt.title('RSI6策略的资金曲线')
# fig.savefig(r'C:\Users\nuonu\Desktop\6.png')

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ["SimHei"]    # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False 
plt.plot(capital_list,color='b')
plt.title('RSI6策略的资金曲线')
plt.show()


#%%

导入某个库后matplotlib画图会出错：
__main__:9: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.


在其他项目都可正常绘图的情况下，则不会是缺少某个库导致的。根本原因是：import导入的某一个库改变了print(matplotlib.get_backend())图像输出位置。
该函数正常情况下返回值为module://matplotlib_inline.backend_inline，而被改变为 Agg。

# 查看matplotlib是否被改变，返回agg则被改变
import matplotlib
print(matplotlib.get_backend())
# 可以重新进入内核看是哪个库改变了mpl图像的输出位置
import pandas as pd
print(matplotlib.get_backend())
import numpy as np
print(matplotlib.get_backend())
import matplotlib.pyplot as plt
print(matplotlib.get_backend())
import matplotlib as mpl
print(matplotlib.get_backend())
import talib
print(matplotlib.get_backend())
import ffn
print(matplotlib.get_backend())

# 发现是ffn改变了mpl图像输出位置

解决方式：
①仅解决显示问题
输入 %matplotlib inline 
可以看到print(matplotlib.get_backend())恢复初始值


②保存图片输出查看
fig=plt.figure()
fig.add_subplot(111)
plt.plot(capital_list,color='r')
plt.title('双均线策略的资金曲线')
plt.show()
fig.savefig(r'C:\Users\nuonu\Desktop\a.png')

③全局重制
在 import hydrofunctions as hf 后将 matplotlib.get_backend() 值重新修改会正常值
matplotlib.use('module://matplotlib_inline.backend_inline')


[Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure 问题](https://blog.csdn.net/a18892061545/article/details/122004704)