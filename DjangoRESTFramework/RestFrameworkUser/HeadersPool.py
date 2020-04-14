from rest_framework import status
from rest_framework.viewsets import ViewSet
from DjangoRESTFramework import models
from rest_framework.response import Response
from DjangoRESTFramework.SerializersModelSData \
    import UserProjectSerializers


class HeadersPools(ViewSet):

    def create_HeadersPool(self, request, *args, **kwargs):
        """创建HeadersPool数据池"""

        verified_data = UserProjectSerializers.HeadersPoolSerializers(data=request.data)

        if verified_data.is_valid():
            verified_data.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def update_HeadersPool(self, request, *args, **kwargs):
        """更新HeadersPool数据池"""

        queryset = models.HeadersPool.objects.filter(
            id=request.data.get("id")).first()
        verified_data = UserProjectSerializers.HeadersPoolSerializers(data=request.data,
                                                                      instance=queryset,
                                                                      many=False)
        if verified_data.is_valid():
            verified_data.save()

            return Response(status=status.HTTP_200_OK, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def get_HeadersPool(self, request, *args, **kwargs):
        """获取HeadersPool数据池"""

        queryset = models.HeadersPool.objects.filter(user=request.user)
        verified_data = UserProjectSerializers.HeadersPoolSerializers(instance=queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=verified_data.data)

    def delete_HeadersPool(self, request, *args, **kwargs):
        """删除HeadersPool数据池"""

        models.HeadersPool.objects.get(id=request.data.get('id'), user=request.user).delete()
        return Response(status=status.HTTP_200_OK, data={"msg": "api info delete successful"})
