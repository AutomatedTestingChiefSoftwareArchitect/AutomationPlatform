from rest_framework import status
from rest_framework.viewsets import ViewSet
from DjangoRESTFramework import models
from rest_framework.response import Response
from DjangoRESTFramework.SerializersModelSData \
    import UserProjectSerializers
from DjangoRESTFramework.RestFrameworkConfig \
    import DataPage


class UserAllProject(ViewSet):

    def user_project(self, request, *args, **kwargs):
        """用户所关联的项目及api"""

        queryset = models.UserProject.objects.filter(user=request.user)
        dataspages = DataPage.DataPageNumberPagination()
        dataspagesrows = dataspages.paginate_queryset(
            queryset=queryset, request=request, view=self)
        verified_data = UserProjectSerializers.UserProjectSerializers(instance=dataspagesrows, many=True)
        return Response(status=status.HTTP_200_OK, data=verified_data.data)

    def create_project(self, request, *args, **kwargs):
        """创建项目"""

        verified_data = UserProjectSerializers.UserProjectSerializer(data=request.data,
                                                                     context={"user": request.user})
        if verified_data.is_valid():
            verified_data.save()

            return Response(verified_data.data, status=status.HTTP_201_CREATED)
        return Response(verified_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_project(self, request, *args, **kwargs):
        """更新项目"""

        queryset = models.UserProject.objects.filter(
            id=request.data.get("id"),
            user=request.user).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"msg": "校验数据不存在！"})

        verified_data = UserProjectSerializers.UserProjectSerializer(
            data=request.data, instance=queryset, many=False)

        if verified_data.is_valid():
            verified_data.save()
            return Response(status=status.HTTP_200_OK, data=verified_data.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=verified_data.errors)

    def delete_project(self, request, *args, **kwargs):
        """删除项目"""

        project_id = request.data.get('id')
        models.UserProject.objects.get(id=project_id, user=request.user).delete()
        return Response(status=status.HTTP_200_OK, data={"msg": "project delete successful"})
