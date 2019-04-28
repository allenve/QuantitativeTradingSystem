from django.shortcuts import render
from django.http import HttpResponse
from .. modules import CompanyCollection
import json

def collectionCompany(request):
    body = json.loads(request.body.decode())
    user_id = body.get('user_id')
    company_id = body.get('company_id')
    username = body.get('username')
    company_name = body.get('company_name')
    ts_code = body.get('ts_code')

    resp = CompanyCollection.userAddCollectionCompany(user_id, company_id, username, company_name, ts_code)

    res_data = {
        "code": resp[0],
        "data": resp[1]
    }

    return res_data

def cancelCollectionCompany(request):
    body = json.loads(request.body.decode())
    user_id = body.get('user_id')
    company_id = body.get('company_id')

    resp = CompanyCollection.userDeleteCollectionCompany(user_id, company_id)

    res_data = {
        "code": resp[0],
        "data": resp[1]
    }

    return res_data

def isCompanyCollection(request):
    body = json.loads(request.body.decode())
    user_id = body.get('user_id')
    company_id = body.get('company_id')
    resp = CompanyCollection.isCollectionCompany(user_id, company_id)

    res_data = {
        "code": resp[0],
        "data": resp[1]
    }
    return res_data