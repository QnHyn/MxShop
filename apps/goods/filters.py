from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # 模糊查询 忽略大小写icontains
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']
