from django_filters import rest_framework as filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # 模糊查询 忽略大小写icontains
    # name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    top_category = filters.NumberFilter(method="top_category_filter")

    # 这是三个参数是默认传递进来的queryset, name, value
    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(Q(category_id=value) | \
                                   Q(category__parent_category_id=value) | \
                                   Q(category__parent_category__parent_category_id=value))
        return queryset


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
