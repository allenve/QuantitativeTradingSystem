from django.db import models
import datetime

class CompanyCollection(models.Model):
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    username = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    ts_code = models.CharField(max_length=30, blank=True)
    createTime = models.DateField(blank=True)

    class Meta():
        db_table = 'company_collection'

# 收藏
def userAddCollectionCompany(user_id, company_id, username, company_name, ts_code):
    collection = CompanyCollection()
    collection.user_id = user_id
    collection.company_id = company_id
    collection.username = username
    collection.company_name = company_name
    collection.ts_code = ts_code
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

