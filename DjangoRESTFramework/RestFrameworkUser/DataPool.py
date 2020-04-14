from rest_framework import status
from rest_framework.viewsets import ViewSet
from DjangoRESTFramework import models
from rest_framework.response import Response
from DjangoRESTFramework.SerializersModelSData \
    import UserProjectSerializers


class DataPools(ViewSet):

    def create_datapool(self, request, *args, **kwargs):
        """创建DataPool数据池"""

        verified_data = UserProjectSerializers.DataPoolSerializers(data=request.data)

        if verified_data.is_valid():
            verified_data.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def update_datapool(self, request, *args, **kwargs):
        """更新DataPool数据池"""

        queryset = models.DataPool.objects.filter(
            id=request.data.get("id")).first()
        verified_data = UserProjectSerializers.DataPoolSerializers(data=request.data,
                                                                   instance=queryset,
                                                                   many=False)
        if verified_data.is_valid():
            verified_data.save()

            return Response(status=status.HTTP_200_OK, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def get_datapool(self, request, *args, **kwargs):
        """获取DataPool数据池"""

        queryset = models.DataPool.objects.filter(user=request.user)
        verified_data = UserProjectSerializers.DataPoolSerializers(instance=queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=verified_data.data)

    def delete_datapool(self, request, *args, **kwargs):
        """删除DataPool数据池"""

        models.DataPool.objects.get(id=request.data.get('id'), user=request.user).delete()
        return Response(status=status.HTTP_200_OK, data={"msg": "api info delete successful"})