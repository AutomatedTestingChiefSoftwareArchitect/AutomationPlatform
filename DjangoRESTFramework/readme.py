"""
models操作指南：

    创建更改的文件 如果提示 No changes detected 那么数据就是同步的
        python manage.py makemigrations
    将生成的py文件应用到数据库
        python manage.py migrate
    查看当前migration文件记录
        python3 manage.py showmigrations

    1、models.AutoField　#如果没有的话，默认会生成一个名称为id的列，如果要显示的定义一个自增列，必须把该列设置为主键(primary_key=True)
    2、models.CharField　#字符串类型字段 必须加max_length参数
    3、models.BooleanField #布尔类型字段=tinyint(1)  不能为空，Blank=True
    4、models.ComaSeparatedIntegerField #用逗号分割的数字类型=varchar 继承CharField，所以必须加max_lenght参数
    5、.models.DateField　#日期字段类型date参数auto_now=True表示每次更新都会更新这个时间；参数auto_now_add表示只是第一次创建时添加，之后的更新不再改变
    6、models.DateTimeField　#日期字段类型datetime  同DateField的参数
    7、models.Decimal　#十进制小数类型=decimal必须指定整数位max_digits和小数位decimal_places
    8、models.EmailField　#字符串类型(正则表达式邮箱)=varchar  对字符串进行正则表达式验证
    9、models.FloatField　#浮点类型=double
    10、models.IntegerField　#整形
    11、models.BigIntegerField　#长整形
    　　integer_field_ranges = {
    　　　　'SmallIntegerField': (-32768, 32767),
    　　　　'IntegerField': (-2147483648, 2147483647),
    　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
    　　　　'PositiveSmallIntegerField': (0, 32767),
    　　　　'PositiveIntegerField': (0, 2147483647),}
    12、models.IPAddressField　　字符串类型(ip4正则表达式)
    13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）参数protocol可以是：both、ipv4、ipv6  验证时，会根据设置进行报错
    14、models.NullBooleanField　　允许为空的布尔类型
    15、models.PositiveIntegerFiel　　正Integer
    16、models.PositiveSmallIntegerField　　正smallInteger
    17、models.SlugField　　减号、下划线、字母、数字
    18、models.SmallIntegerField　　数字数据库中的字段有：tinyint、smallint、int、bigint
    19、models.TextField　　字符串=longtext
    20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
    21、models.URLField　　字符串类型，地址正则表达式
    22、models.BinaryField　二进制
    23、models.ImageField   图片
    24、models.FilePathField 文件

    Django生命周期：
        前端发送请求-->Django的wsgi-->中间件-->路由系统-->视图-->ORM数据库操作-->模板-->返回数据给用户

    django rest framework生命周期：
        发送请求-->Django的wsgi-->中间件-->路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->在执行dispath之前，
        有版本分析 和 渲染器-->在dispath内，对request封装-->版本-->认证-->权限-->限流-->视图-->
        如果视图用到缓存( request.data or request.query_params )就用到了 解析器-->视图处理数据，用到了序列化(对数据进行序列化或验证)
        -->视图返回数据可以用到分页

200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

"""