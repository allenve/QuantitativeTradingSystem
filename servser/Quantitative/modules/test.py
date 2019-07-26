# 或许数据并存储到数据库
import tushare as ts
ts.set_token('bb72e0cc0b36f9a154fae491cd4a06f71986d609c787c801dc7b3086')

import MySQLdb
import pandas as pd
from sqlalchemy import create_engine
host = '119.23.74.116'
port = 3306
db = 'graduation'
user = 'root'
password = 'yupeng'
engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,password,host,port,db))

# 更新股票公司信息
def saveStockCompany():
    pro = ts.pro_api()
    # df = pro.stock_company(exchange='SZSE', fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')# print(data)
    df = pro.stock_company(exchange='SSE', fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')# print(data)
    stock_data = df.to_json(orient="index")

    try:
        df.to_sql('stock_company_detail',con=engine,if_exists='append',index=False)
        print("success")
    except Exception as e:
        print(e)

saveStockCompany()

def saveTsCodeWithCompany():
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    try:
        data.to_sql('stock_company',con=engine,if_exists='append',index=False)
        print("success")
    except Exception as e:
        print(e)
# saveTsCodeWithCompany()