#%%
import pandas as pd
stock_data=pd.read_csv(r'F:\assert\pycodedemo\datademo\sh000001.csv',parse_dates=[1])
stock_data.head()

#将数据按照交易日从远到近排序 (小→大)
stock_data.sort_values('date',inplace=True)

#计算5、20、60日移动平均线 MA
ma_list=[5,20,60]
for ma in ma_list:
    stock_data['MA_'+str(ma)]=stock_data.close.rolling(ma).mean()
    
#计算指数平滑移动平均线EMA
for ma in ma_list:
    stock_data['EMA_'+str(ma)]=pd.DataFrame.ewm(stock_data.close,span=ma).mean()

# 将数据按照交易日期从近到远排序
stock_data.sort_values('date', ascending=False, inplace=True)

#将算好的数据输出到csv文件
stock_data.to_csv(r'F:\assert\pycodedemo\datademo\sh600000_ma_ema.csv', index=False)

#%%
# 2022-5-25
# 下面是函数的使用，注意在计算指标时，要把日期都从小到大排列

import talib
import pandas as pd
data=pd.read_csv(r'F:\assert\pycodedemo\datademo\sh000001.csv',parse_dates=[1])
data.sort_values('date',inplace=True)


# 1.简单移动平均指标SMA
# 参数说明：talib.SMA(a,b)
# a:要计算平均数的序列；b:计算平均线的周期。表示计算a的b日移动平均
# 未知参数1个，是b--天数，要给出计算的天数
period=5
data['SMA_'+str(period)]=talib.SMA(data.close.values,5)



# 2. CCI ：顺势指标
# real = CCI(high, low, close, timeperiod=14)
# 参数说明：high:最高价；low:最低价；close：收盘价；timeperiod：时间周期
# 未知参数1个，是timeperiod--天数，要给出计算的天数
timeperiod=14
data['CCI_'+str(timeperiod)]= talib.CCI(data['high'].values, data['low'].values,data.close.values, timeperiod)



# 3. RSI：相对强弱指数
# real = RSI(close, timeperiod=14)
# 参数说明：close：收盘价；timeperiod：时间周期
# 未知参数1个，是timeperiod--天数，要给出计算的天数
timeperiod=14
data['RSI_'+str(timeperiod)]= talib.RSI(data.close.values, timeperiod)




# 4. MACD:平滑异同移动平均线
# macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
# 参数说明：high:最高价；low:最低价；close：收盘价；fastperiod:快周期； slowperiod：慢周期
# 未知参数3个，；fastperiod:快周期； slowperiod：慢周期；signalperiod=9
fastperiod=12
slowperiod=26
signalperiod=9

data['MACD_macd'],data['MACD_macdsignal'],data['MACD_macdhist']= talib.MACD(data.close.values, fastperiod, slowperiod, signalperiod)







# 5.OBV：能量潮
# OBV(close, volume)
# 参数说明：close:收盘价,volume:成交量
data['OBV'] = talib.OBV(data.close.values, data['volume'])













