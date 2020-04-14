from rest_framework import serializers
from DjangoRESTFramework import models


class InterfaceSerializers(serializers.ModelSerializer):
    """序列化保存接口信息 - Platforminterface"""

    data = serializers.JSONField()
    headers = serializers.JSONField()
    expectedresults = serializers.JSONField()

    class Meta:
        model = models.UserApiInfo
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        return models.UserApiInfo.objects.create(**validated_data)


class DataPoolSerializer(serializers.ModelSerializer):
    """个人datakey数据池数据序列化"""

    datakey = serializers.CharField()

    class Meta:
        model = models.DataPool
        fields = ["datakey"]


class DataPoolSerializers(serializers.ModelSerializer):
    """个人datavalue数据池数据序列化"""

    datavalue = serializers.CharField()

    class Meta:
        model = models.DataPool
        fields = ["datavalue"]


class HeadersPoolSerializer(serializers.ModelSerializer):
    """个人headers数据池数据序列化"""

    datakey = serializers.CharField()

    class Meta:
        model = models.HeadersPool
        fields = ["datakey"]


class HeadersPoolSerializers(serializers.ModelSerializer):
    """个人headers数据池数据序列化"""

    datavalue = serializers.CharField()

    class Meta:
        model = models.HeadersPool
        fields = ["datavalue"]