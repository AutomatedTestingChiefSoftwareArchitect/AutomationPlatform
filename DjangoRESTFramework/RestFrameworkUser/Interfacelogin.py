from rest_framework import status
from rest_framework.views import APIView
from DjangoRESTFramework import models
from rest_framework.response import Response
from DjangoRESTFramework.RestFrameworkConfig import UserToken


class AuthView(APIView):
    """用户登录
                ↓List is None无需任何鉴权"""

    throttle_classes = []
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        try:

            user_name = request.data.get('user_name')
            user_pwd = request.data.get('password')
            queryset = models.UserInfo.objects.filter(user_name=user_name, password=user_pwd).first()

            if not queryset:

                return Response(status=status.HTTP_404_NOT_FOUND, data={'msg': '用户名或密码错误!'})

            usertoken = UserToken.TokenEncryption(user_name)

            models.UserToken.objects.update_or_create(user=queryset, defaults={'user_token': usertoken})

            return Response(status=status.HTTP_200_OK,
                            data={'msg': '登录成功!', 'user_name': user_name, 'password': user_pwd,
                                  'user_type': queryset.user_type, 'user_token': usertoken})

        except Exception as LoginError:

            return Response(status=status.HTTP_400_BAD_REQUEST, data={'msg': 'Error:' + str(LoginError)})