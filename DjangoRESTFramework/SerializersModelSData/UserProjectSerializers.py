from rest_framework import serializers
from DjangoRESTFramework import models
from DjangoRESTFramework.SerializersModelSData \
    import InterfaceSerializers


class UserProjectSerializers(serializers.ModelSerializer):
    """用户项目 - user_project"""

    # 嵌套序列化返回 用户项目所关联的api
    project = InterfaceSerializers.InterfaceSerializers(many=True, source='api_info')

    class Meta:
        model = models.UserProject
        fields = "__all__"
        depth = 1  # 指定深度-- 返回项目所关联的用户
        # exclude = ('users', ) 返回排除字段


class UserProjectSerializer(serializers.ModelSerializer):
    """用户项目 - create_project"""

    class Meta:
        model = models.UserProject
        fields = "__all__"

    user = serializers.SerializerMethodField()  # 自定义字段

    def get_user(self, obj):
        # 处理自定义的字段返回user_id, 通过外键获取UserInfo的数据
        return obj.user.id

    def create(self, validated_data):
        # 处理外键user字段
        return models.UserProject.objects.create(user=self.context["user"],
                                                 **validated_data)


class DataPoolSerializers(serializers.ModelSerializer):
    """个人datavalue数据池数据序列化"""

    class Meta:
        model = models.DataPool
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}


class HeadersPoolSerializers(serializers.ModelSerializer):
    """个人headers数据池数据序列化"""

    class Meta:
        model = models.HeadersPool
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}