from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer功能比Serializer更强大 和之前的ModelForm 差不多
class GoodsSerializer(serializers.ModelSerializer):
    # 3. 获取外键的所有信息 实例化GoodsCategorySerializer 覆盖原有的字段
    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        # 1. 更简单 从Model中直接映射
        # fields = ['name', 'click_num', 'market_price', 'add_time']
        # 2. 取出全部 外键序列化为id
        fields = "__all__"

