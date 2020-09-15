from goods.serializer import GoodsSerializer
from rest_framework import generics
from .models import Goods
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend


# 自定义分页的样式
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页展示
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'shop_price']


    # 重载get函数
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # 加自己逻辑 过滤数据
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     # 前端穿过来的数据
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = Goods.objects.filter(shop_price__gt=int(price_min))
    #     return queryset
        #return Goods.objects.filter(shop_price__gt=100)

