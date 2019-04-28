# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
 
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class SessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        # 需要登录的api
        need_login = [
            '/api/setUserInfo',
            '/api/loginout',
            # '/api/collectionCompany',
            # '/api/isCompanyCollection',
            # '/api/cancelCollectionCompany',
            '/api/needlogin'
        ]
        # 需要登录验证
        if request.path in need_login:
            
            print(request.user.is_authenticated)
            if not request.user.is_authenticated:
                print('未登录或登录已过期')
                resp = {
                    'code': 2001,
                    'data': {
                        'msg': '未登录或登录已过期'
                    }
                }
                return HttpResponse(json.dumps(resp), content_type="application/json")
        # 不需要登录验证
        # else:
        response = self.get_response(request)
        return response
        # session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        # request.session = self.SessionStore(session_key)

    # def process_response(self, request, response):
    #     print("SessionMiddleware: process_response")
    #     return HttpResponse(response)