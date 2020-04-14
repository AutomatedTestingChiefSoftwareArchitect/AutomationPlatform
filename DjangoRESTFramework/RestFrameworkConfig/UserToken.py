# coding=utf-8
from rest_framework import exceptions
from DjangoRESTFramework import models
from rest_framework.authentication import BaseAuthentication


def TokenEncryption(user_name):
    """生成随机Token"""

    import time
    import hashlib
    ctime = str(time.time())
    Encryption = hashlib.md5(bytes(user_name, encoding='utf-8'))
    Encryption.update(bytes(ctime, encoding='utf-8'))
    return Encryption.hexdigest()


class Authtication(BaseAuthentication):
    """重写全局访问认证Authtication方法"""

    def authenticate(self, request):
        Global_token = request.data.get('user_token')
        Token_object = models.UserToken.objects.filter(user_token=Global_token).first()
        if not Token_object:
            raise exceptions.AuthenticationFailed('Token Check Error')
        # rest_framework内部已赋值给request以供后续使用request.user = Token_object.user, request.auth = Token_object
        return Token_object.user, Token_object

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass
