from django.db import models
from django.db.models import Q
import json

class StockCompanyDetail(models.Model):
    ts_code = models.CharField(max_length=20) #股票代码
    exchange = models.CharField(max_length=10, blank=True) #交易所代码 ，SSE上交所 SZSE深交所
    chairman = models.CharField(max_length=30, blank=True) #法人代表
    manager = models.CharField(max_length=30, blank=True) #总经理
    secretary = models.CharField(max_length=30, blank=True) #董秘
    reg_capital = models.FloatField(blank=True) #注册资本
    setup_date = models.DateField(blank=True) #注册日期
    province = models.CharField(max_length=30, blank=True) #所在省份
    city = models.CharField(max_length=30, blank=True) #所在城市
    introduction = models.CharField(max_length=3000, blank=True) #公司介绍
    website = models.CharField(max_length=100, blank=True) #公司主页
    email = models.CharField(max_length=500, blank=True) #电子邮件
    office = models.CharField(max_length=2000, blank=True) #办公室
    employees = models.FloatField(max_length=20, blank=True) #员工人数
    main_business = models.CharField(max_length=500, blank=True) #主要业务及产品
    business_scope = models.CharField(max_length=3000, blank=True) #经营范围

    class Meta():
        db_table = 'stock_company_detail'

class StockCompany(models.Model):
    ts_code = models.CharField(max_length=20) #TS代码
    symbol = models.CharField(max_length=20) #股票代码
    name = models.CharField(max_length=50) #股票名称
    area = models.CharField(max_length=50) #所在地狱
    industry = models.CharField(max_length=100) #所属行业
    fullname = models.CharField(max_length=200) #股票全称
    enname = models.CharField(max_length=255) #英文全称
    market = models.CharField(max_length=50) #市场类型 （主板/中小板/创业板）
    exchange = models.CharField(max_length=10) #交易所代码
    curr_type = models.CharField(max_length=50) #交易货币
    list_status = models.CharField(max_length=10) #上市状态： L上市 D退市 P暂停上市
    list_date = models.DateField(blank=True) #上市日期
    delist_date = models.DateField(blank=True) #退市日期
    is_hs = models.CharField(max_length=20) #是否沪深港通标的，N否 H沪股通 S深股通


    class Meta():
        db_table = 'stock_company'

# 获取L上市 D退市 P暂停上市 股票列表
def getStockCompany(list_status, limit, pagenum):
    status = list_status or 'L'
    company_list = []
    try:
        company_lists = StockCompany.objects.all()[limit*(pagenum-1):limit*pagenum]
        # company_lists = StockCompany.objects.all()[0:limit]
        count = StockCompany.objects.count()
        for company in company_lists:
            json_dict = {}
            json_dict["id"] = str(company.id) or ''
            json_dict["ts_code"] = str(company.ts_code) or ''
            json_dict["name"] = str(company.name) or ''
            json_dict["area"] = str(company.area) or ''
            json_dict["industry"] = str(company.industry) or ''
            json_dict["fullname"] = str(company.fullname) or ''
            json_dict["exchange"] = str(company.exchange) or ''
            json_dict["list_status"] = str(company.list_status) or ''
            company_list.append(json_dict)

        res_company_data = {
            "company_list":  company_list,
            "count": count,
            "nowPage": pagenum
        }
        return [200, res_company_data]
    
    except Exception as e:
        print("failed")
        return [201, {"msg": str(e)}]

# 通过公司姓名模糊查询
def searchStockCompanyByName(name):
    company_list = []

    try:
        company_lists = StockCompany.objects.filter(Q(name__icontains=name)|Q(fullname__icontains=name))[:20]
        
        for company in company_lists:
            json_dict = {}
            json_dict["ts_code"] = str(company.ts_code) or ''
            json_dict["name"] = str(company.name) or ''
            json_dict["area"] = str(company.area) or ''
            json_dict["industry"] = str(company.industry) or ''
            json_dict["fullname"] = str(company.fullname) or ''
            json_dict["exchange"] = str(company.exchange) or ''
            json_dict["list_status"] = str(company.list_status) or ''
            company_list.append(json_dict)

        res_company_data = {
            "company_list":  company_list
        }

        return [200, res_company_data]
    except Exception as e:
        print(e)
        return [201, {"msg": str(e)}]


# 通过股票代码或许公司相信信息
def searchStockCompanyByTsCode(ts_code):
    try:
        company_data = StockCompanyDetail.objects.get(ts_code=ts_code)
        res_company_data = {
            "ts_code": str(company_data.ts_code) or "",
            "exchange": str(company_data.exchange) or "",
            "chairman": str(company_data.chairman) or "",
            "manager": str(company_data.manager) or "",
            "secretary": str(company_data.secretary) or "",
            "reg_capital": str(company_data.reg_capital) or "",
            "setup_date": str(company_data.setup_date) or "",
            "province": str(company_data.province) or "",
            "city": str(company_data.city) or "",
            "introduction": str(company_data.introduction) or "",
            "website": str(company_data.website) or "",
            "email": str(company_data.email) or "",
            "office": str(company_data.office) or "",
            "employees": str(company_data.employees) or "",
            "main_business": str(company_data.main_business) or "",
            "business_scope": str(company_data.business_scope) or ""
        }
        return [200, res_company_data]
    except Exception as e:
        print(e)
        return [201, {"msg": str(e)}]








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
    df = pro.stock_company(exchange='SZSE', fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')# print(data)
    stock_data = df.to_json(orient="index")

    try:
        df.to_sql('stock_company_detail',con=engine,if_exists='fail',index=False)
        print("success")
    except Exception as e:
        print(e)
    resp = {
        "success": "ok",
        "data": {
            'msg': '更新成功'
        }
    }
    return resp



def saveTsCodeWithCompany():
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    try:
        data.to_sql('stock_company',con=engine,if_exists='fail',index=False)
        print("success")
    except Exception as e:
        print(e)
    # print(data)

    return {
        'msg': 'success'
    }