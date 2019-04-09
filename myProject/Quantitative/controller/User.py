from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from ..middleware.decorator import logged_in
from ..modules import Users
import json

# 注册
def register(request):
    body = json.loads(request.body.decode())
    username = body.get('username')
    password = body.get('password')
    email = body.get('email')
    
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True
        try:
            user.save()
            resp = {
                'code': 200,
                'data': {
                    'msg': '注册成功'
                }
            }
            return resp
        except:
            return {
                'code': 201,
                'data': {
                    'msg': '注册失败'
                }
            }
    except:
        return {
            'code': 201,
            'data': {
                'msg': '该用户名已存在'
            }
        }
    
# 登录
def login(request):
    body = json.loads(request.body.decode())
    username = body.get('username')
    password = body.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        print("user login")
        user_data_resp = Users.getUserInfo(user.username)
        resp = {
            'code': 200,
            'data': {
                'msg': '登录成功',
                'data': user_data_resp
            }
        }
        return resp
    else:
        return {
            'code': 201,
            'data': {
                'msg': '账号或密码错误'
            }
        }

# 登出
def loginout(request):
    auth.logout(request)
    return {
        'code': 200,
        'data': {
            'msg': '成功退出'
        }
    }

# 修改用户信息
def setUserInfo(request):
    body = json.loads(request.body.decode())
    user_id = body.get('id')
    nickname = body.get('nickname')
    mobile = body.get('mobile')
    email = body.get('email')
    sex = body.get('sex')
    city = body.get('city')
    signature = body.get('signature')
    print(signature)
    resp = Users.setUserInfo(user_id, nickname, mobile, email, sex, city, signature)

    return {
        'code': resp[0],
        'data': resp[1]
    }
