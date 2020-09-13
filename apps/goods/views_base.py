from django.views.generic.base import View
from goods.models import Goods


class GoodsListView(View):
    # 重载get方法 默认传递request
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        # 先获取十条 防止加载过慢
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     # 这里注意 不能对datetime类型序列化 Object of type 'datetime' is not JSON serializable
        #     # json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)

        # 1. 解决手动填充的问题 工作量大 易出错 但是解决不了datetime和ImageFieldFile字段序列化的问题。
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 2. 同时解决所有字段序列化 和 手动填充问题
        from django.core import serializers
        json_data = serializers.serialize("json", goods)

        # 这里HttpResponse需要传入 序列化后的字符串
        # from django.http import HttpResponse
        # return HttpResponse(json_data, content_type="application/json")

        # 这里JsonResponse需要传入 List对象 刚好和HttpResponse传入的相反
        from django.http import JsonResponse
        import json
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)

