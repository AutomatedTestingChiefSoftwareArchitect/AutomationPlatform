from rest_framework.pagination import LimitOffsetPagination


class DataPageNumberPagination(LimitOffsetPagination):

    default_limit = 10
    limit_query_param = 'pageSize'
    offset_query_param = 'pageIndex'
    max_limit = 50  # pageIndex最大值
