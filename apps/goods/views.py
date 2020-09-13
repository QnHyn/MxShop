from goods.serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods


# APIView 集成 django中的view 而且加了很多功能
class GoodsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        # many=True 列表里面有十个 如果只是一个可以不加
        goods_json = GoodsSerializer(goods, many=True)
        return Response(goods_json.data)

