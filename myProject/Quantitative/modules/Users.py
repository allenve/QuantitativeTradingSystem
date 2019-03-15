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