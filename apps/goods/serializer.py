from rest_framework import serializers


# 功能很强大 和之前的forms.py 差不多 支持序列化json
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()