# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:50:16 2022

@author: nuonu
"""
import pandas as pd
import numpy as np

# 大类：
# ①列出发
# data={key:value}
# key 为列名；
# value有三种形式，但都存列数据；ndarray、series、dict
# # data={'key=列':ndarray,'key':ndarray,...}
# # data={'key=列':series,'key':series,...}
# # data={'key=列':{},'key':{},...}

# ②行出发
# #这里{}存行数据，每个dict里是键值对，key=列名，value当前行当前列的值
# # ④data=[{},{},...]
# # [{'four':4,'one':1,'three':3,'two':2},...]

# ③二维数据出发
# 2darray


#%%
# data={'key=列':ndarray,'key':ndarray,...}
# ndarray装列数据
#①字典dict直接创建
#一个键值对代表一列，键为列名，有多少个值就有多少个样本，转成DF时可以指定行名
#key=列名  :  value=ndarray

data1 = {'four':np.arange(4,9), 'one':range(1,6), 'three':[3,4,5,6,7],'two':range(2,7)}
print('(1) 由列表组成的字典')
print(pd.DataFrame(data1, index=list('abcde')))
print('------------')

#%%
# data={'key':series,'key':series,...}
# series装列数据
#②字典dict直接创建
#一个键值对代表一列，键为列名，有多少个值就有多少个样本，
#key=列名  :  value=Series
#Series可以指定index，在转化成DF时就不用指定index了


data2 = {'four':pd.Series(np.arange(4,9), index=list('abcde')), 
         'one':pd.Series(range(1,6), index=list('abcde')),
         'three':pd.Series((3,4,5,6,7), index=list('abcde')),
         'two':pd.Series(range(2,7), index=list('abcde'))}
print('(2) 由Series组成的字典')
print(pd.DataFrame(data2))
print('------------')


#%%
# data=2darray
#③二维数组建立DF，index，columns在生成DF时指定
data3=np.array([4,1,3,2,5,2,4,3,6,3,5,4,7,4,6,5,8,5,7,6]).reshape(5,4)
print('(3)通过二维数组直接创建')
print(pd.DataFrame(data3, index=list('abcde'), columns=['four', 'one', 'three', 'two']))
print('------------')

#%%
# ④data=[{},{},...]
#这里{}存行数据
data4 = [{'four':4,'one':1,'three':3,'two':2}, {'four':5,'one':2,'three':4,'two':3},
         {'four':6,'one':3,'three':5,'two':4}, {'four':7,'one':4,'three':6,'two':5}, 
        {'four':8,'one':5,'three':7,'two':6}]
print('(4)由字典组成的列表')
# print(pd.DataFrame(data4, index=list('abcde')))
print(pd.DataFrame(data4, index=list('abcde'),columns=['one','four'])) #可以选择要的列
print('------------')

#%%
# data={'key=列':dict,'key':dict,...}
# data={'key=列':{},'key':{},...}
#{}装列数据
data5 = {'four':{'a':4, 'b':5, 'c':6, 'd':7, 'e':8}, 
        'one':{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}, 
        'three':{'a':3, 'b':4, 'c':5, 'd':6, 'e':7}, 
        'two':{'a':2, 'b':3, 'c':4, 'd':5, 'e':6}}
print('(5)由字典组成的字典')
print(pd.DataFrame(data5, index=list('abcde')))
print(pd.DataFrame(data5, index=list('abcde'), columns=[ 'two','four', 'one', 'three'])) #改变列顺序
# print(pd.DataFrame(data5, index=list('abcde'), columns=['four', 'one', 'three', 'two']))

