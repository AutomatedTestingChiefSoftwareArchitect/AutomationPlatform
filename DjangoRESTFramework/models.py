from django.db import models


class UserInfo(models.Model):
    """用户信息"""

    user_type_choices = ((1, 'user'), (6, 'admin'))
    id = models.AutoField(primary_key=True, verbose_name='user_id')
    user_name = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    user_type = models.IntegerField(choices=user_type_choices, verbose_name='用户类型')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return str(self.id)


class UserToken(models.Model):
    """用户Token"""

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    user_token = models.CharField(max_length=64, verbose_name='用户Token')
    """OneToOneField的第一个参数是被关联的模型的名称，第二个参数表示级联删除"""
    user = models.OneToOneField(to='UserInfo', related_name='api_user', on_delete=models.CASCADE,
                                verbose_name='一对一用户关联')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.user_token


class UserProject(models.Model):
    """用户项目"""

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    name = models.CharField(max_length=50, verbose_name='项目名称')
    description = models.CharField(max_length=1024, null=True, verbose_name='描述')
    user = models.ForeignKey(to='UserInfo', related_name='api_project',
                             on_delete=models.CASCADE, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')


class UserApiInfo(models.Model):
    """项目接口信息"""

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    project = models.ForeignKey(to='UserProject', related_name='api_info',
                                on_delete=models.CASCADE, verbose_name='所属项目')
    url = models.URLField(max_length=1024, verbose_name='接口名称')
    method = models.CharField(max_length=32, verbose_name='请求方法(GET, POST)')
    data = models.CharField(max_length=1024, verbose_name='接口数据')
    headers = models.CharField(max_length=1024, verbose_name='请求头')
    expectedresults = models.CharField(max_length=64, blank=True, null=True, verbose_name='预期结果')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    user = models.ForeignKey(to='UserInfo', related_name='user_api', on_delete=models.CASCADE,
                             verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')


class DataPool(models.Model):
    """data数据池"""

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    datakey = models.CharField(max_length=64, verbose_name='数据key')
    datavalue = models.CharField(max_length=64, verbose_name='数据value')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    user = models.ForeignKey(to='UserInfo', related_name='data_pool', on_delete=models.CASCADE,
                                verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')


class HeadersPool(models.Model):
    """headers数据池"""

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    datakey = models.CharField(max_length=64, verbose_name='数据key')
    datavalue = models.CharField(max_length=64, verbose_name='数据value')
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    user = models.ForeignKey(to='UserInfo', related_name='headers_pool', on_delete=models.CASCADE,
                                verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='创建时间')