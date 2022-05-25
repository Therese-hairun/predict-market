from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class SubscribeLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class SubscribePageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"


class ClientLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


class ClientPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "size"
    max_page_size = 1000


class ReductionCodePageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"


class RewardLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class RewardPageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"


class InvoicePageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"



class CouplePageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"


class LogPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "size"
    max_page_size = 1000