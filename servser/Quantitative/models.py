from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=1, blank=True)
    city = models.CharField(max_length=255, blank=True)
    signature = models.CharField(max_length=255, blank=True)

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'

def register(username, email, password):
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.save()
        resp = {
            'code': 200,
            'data': {
                'msg': '注册成功'
            }
        }
        return resp
    except Exception as e:
        print(e)
        return {
            'code': 201,
            'data': {
                'msg': e
            }
        }

def changePassword(id, oldPsd, newPsd):
    try:
        user = User.objects.get(id=id)
        checkPsd = user.check_password(oldPsd)
        if checkPsd and newPsd:
            user.set_password(newPsd)
            user.save()
            return [200, '修改密码成功']
        else:
            return [201, '旧密码错误']
    except Exception as e:
        print(e)
        return [201, str(e)]


def getUserInfo(username):
    try:
        user_data = User.objects.get(username=username)
        new_user_data = {
            'id': user_data.id,
            'username': user_data.username,
            'nickname': user_data.nickname or '',
            'mobile': user_data.mobile or '',
            'email': user_data.email or '',
            'sex': user_data.sex or '',
            'city': user_data.city or '',
            'signature': user_data.signature or ''
        }
        return new_user_data
    except:
        return '获取用户信息失败'

def setUserInfo(user_id, nickname, mobile, email, sex, city, signature):
    # 获取user对象
    # User.objects.filter(id=user_id).update(nickname=nickname, mobile=mobile, sex=sex, city=city, signature=signature)
    try:
        User.objects.filter(id=user_id).update(nickname=nickname, mobile=mobile, email=email, sex=sex, city=city, signature=signature)
        user_data = User.objects.get(id=user_id)
        new_user_data = {
            'id': user_data.id,
            'username': user_data.username,
            'nickname': user_data.nickname,
            'mobile': user_data.mobile,
            'email': user_data.email,
            'sex': user_data.sex,
            'city': user_data.city,
            'signature': user_data.signature
        }
        return [200, {'msg': '修改用户信息成功', 'data': new_user_data}]
    except:
        return [400, {'msg': '修改用户信息失败'}]
    # print(User.objects.filter(username=username))
    # print(same_user_username)