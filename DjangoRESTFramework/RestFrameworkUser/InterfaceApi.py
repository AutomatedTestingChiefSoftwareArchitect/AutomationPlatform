from rest_framework import status
from rest_framework.viewsets import ViewSet
from DjangoRESTFramework import models
from rest_framework.response import Response
from DjangoRESTFramework.SerializersModelSData \
    import InterfaceSerializers


class UserApiInfoView(ViewSet):

    def api_save(self, request, *args, **kwargs):
        """保存接口"""

        verified_data = InterfaceSerializers.InterfaceSerializers(data=request.data)

        if verified_data.is_valid():
            verified_data.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def update_api(self, request, *args, **kwargs):
        """更新api"""

        queryset = models.UserApiInfo.objects.filter(
                        id=request.data.get("id")).first()
        verified_data = InterfaceSerializers.InterfaceSerializers(data=request.data,
                                                                  instance=queryset,
                                                                  many=False)
        if verified_data.is_valid():
            verified_data.save()

            return Response(status=status.HTTP_200_OK, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def delete_api(self, request, *args, **kwargs):
        """删除api"""

        info_id = request.data.get('id')
        models.UserProject.objects.get(id=info_id, user=request.user).delete()
        return Response(status=status.HTTP_200_OK, data={"msg": "api info delete successful"})