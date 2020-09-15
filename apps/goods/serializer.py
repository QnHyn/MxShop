from rest_framework import serializers
from goods.models import Goods


# 功能很强大 和之前的forms.py 差不多 支持序列化json
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    # 这个字段会根据 django设置的路径自动加上 如下图
    goods_front_image = serializers.ImageField()

    # 用来保存 将上面字段全放到validated_data中
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # 这里可以保存前段的数据
        return Goods.objects.create(**validated_data)