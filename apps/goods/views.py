from goods.serializer import GoodsSerializer
from rest_framework import generics
from .models import Goods
from rest_framework.pagination import PageNumberPagination


# 自定义分页的样式
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 必须继承ListModelMixin和GenericAPIView, 如果要接受前端发来数据还要继承CreateModelMixin
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
# ListAPIView 查看源码它帮我们继承了ListModelMixin和GenericAPIView 并重写了get方法
class GoodsListView(generics.ListAPIView):
    """
    商品列表页展示
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # 重载get函数
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

