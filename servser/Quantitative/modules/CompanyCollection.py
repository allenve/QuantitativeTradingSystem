from django.db import models
import datetime

class CompanyCollection(models.Model):
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    username = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    ts_code = models.CharField(max_length=30, blank=True)
    fullname = models.CharField(max_length=150, blank=True)
    createTime = models.DateField(blank=True)

    class Meta():
        db_table = 'company_collection'

# 收藏
def userAddCollectionCompany(user_id, company_id, username, company_name, ts_code, fullname):
    collection = CompanyCollection()
    collection.user_id = user_id
    collection.company_id = company_id
    collection.username = username
    collection.company_name = company_name
    collection.ts_code = ts_code
    collection.fullname = fullname
    collection.createTime = datetime.datetime.now()
    try:
        collection.save()
        return [200, {'msg': "收藏成功", "isCollection": True}]

    except Exception as e:
        return [201, {"msg": str(e)}]

# 取消收藏
def userDeleteCollectionCompany(user_id, company_id):
    try:
        delete_item = CompanyCollection.objects.get(user_id=user_id,company_id=company_id).delete()
        return [200, {"msg": "取消收藏成功", "isCollection": False}]
    except Exception as e:
        print(e)
        return [201, {"msg": str(e)}]

# 检查是否收藏
def isCollectionCompany(user_id, company_id):
    try:
        collection = CompanyCollection.objects.filter(user_id=user_id, company_id=company_id)
        isCollection = False
        if collection:
            isCollection = True
        return [200, {"isCollection": isCollection}]
        
        

    except Exception as e:
        print(e)
        return [201, {"msg": str(e)}]

# 获取用户的收藏列表
def getUserCollectCompany(user_id, limit, pagenum):
    company_list = []
    try:
        list = []
        if limit and pagenum:
            list = CompanyCollection.objects.filter(user_id=user_id)[limit*(pagenum-1):limit*pagenum]
        else:
            list = CompanyCollection.objects.filter(user_id=user_id)
        count = list.count()
        for item in list:
            json_dict = {}
            json_dict["company_id"] = str(item.company_id)
            json_dict["ts_code"] = str(item.ts_code)
            json_dict["company_name"] = str(item.company_name)
            json_dict["fullname"] = str(item.fullname)
            json_dict["createTime"] = item.createTime.strftime('%Y-%m-%d')
            company_list.append(json_dict)

        res_company_data = {
            "list":  company_list,
            "count": count,
            "nowPage": pagenum
        }
        return [200, res_company_data]

    except Exception as e:
        print(e)
        return [201, {"msg": str(e)}]

