import tushare as ts
import pandas as pd
import time
import os

# os.chdir('E:/all_trading_data/')  #保存的绝对路径
# ts.set_token('14d2175349cf92949942d9eb02b8b0be887e0ef21ab6999a5fec439c')
# # pro = ts.pro_api('14d2175349cf92949942d9eb02b8b0be887e0ef21ab6999a5fec439c')
#
# pd.set_option('expand_frame_repr', False)#True就是可以换行显示。设置成False的时候不允许换行
pd.set_option('display.max_columns', None)# 显示所有列
pd.set_option('display.max_rows', None)# 显示所有行
# pd.set_option('colheader_justify', 'centre')# 显示居中
#
# #df_daily = pro.daily()  获取所有股票日行情信息
# #df_basic = pro.stock_basic()  获取所有股票基本信息
# # trade_d = pro.trade_cal(exchange='SSE', is_open='1', start_date=20200101, end_date=20200201, fields='cal_date')
# #
# # df_daily = pro.daily(trade_date=20200106)
# df_basic = ts.pro_bar(ts_code='000001.SH', asset='I', freq='30min',start_date='20190101', end_date='20190111')
# print(df_basic)
# def get_all_stockdata(st_date, ed_date):
#     trade_d = pro.trade_cal(exchange='SSE', is_open='1', , start_date='20200103', end_date='20200109', fields='cal_date')
#
#     for date in trade_d['cal_date'].values:
#         # 先获得所有股票的行情数据
#         df_daily = pro.daily(trade_date=date)
#
#         # 再获取所有股票的基本信息
#         df_basic = pro.stock_basic()
#
#         #行情数据跟基本信息数据合并生成一个csv数据文件
#         #on='ts_code'以ts_code为索引，合并数据，how='outer'，取并集
#         df_all = pd.merge(left=df_basic, right=df_daily, on='ts_code', how='outer')
#         #删除symbol列数据，跟ts_code数据重复
#         df_all = df_all.drop('symbol', axis=1)
#         #强制转换成str字符串格式
#         df_all['ts_code'] = df_all['ts_code'].astype(str)
#
#         # 保存数据，不保存索引，如果index=True，则保存索引会多出一列
#         df_all.to_csv(str(date) + '_ts.csv', index=False, encoding='gbk')
#         print(df_all)
#         print('%s is downloaded.' % (str(date)))
#     return df_all
# if __name__=="__main__":
# 	get_all_stockdata('20200101', '20200315')

# fpath = 'E:/all_trading_data/20200102_ts.csv'
# data = pd.read_csv(fpath,encoding="unicode_escape")
# print(data.head())
# print(data.shape)
# print(data.index)
# print(data.dtypes)
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# # 1 导入 csv 文件
i = pd.read_csv(r"E:\all_trading_data\20200102_ts.csv",encoding="gbk") #由于文件中有中文，因此必须编码
pd.set_option('display.max_rows', None)# 显示所有行
print(i.head())  # 统计分析
j=i[12:18]
k=j[['vol','amount']]
line = pd.DataFrame(k,columns=['amount'])
line.plot()
plt.show()

print(k)



# pd.concat([df1,df2],axis=0)

# path=r'E:\all_trading_data'        #批量表格所在文件路径
# file=glob.glob(os.path.join(path, "20200***_ts.csv"))      #每一个表格相同名称部分
# # print(file)
#
# dl= []
# for f in file:
#     dl.append(pd.read_csv(f,index_col=None,encoding='ANSI'))     #读取每个表格
# df=pd.concat(dl)
# # print(df.head(5))
# ndf=df[['ts_code', 'open','close','high','trade_date']]
# newdf =ndf[ndf['open']*1.09 < ndf['close']]
# newdf =pd.DataFrame(newdf)
# f3_and_e2 = df.columns[3::2]
# # for i in f3_and_e2:
# #
# #     i+=1




