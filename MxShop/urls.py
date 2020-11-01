"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
import rest_framework
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
# from goods.views_base import GoodsListView
from goods.views import GoodsListViewset, CategoryViewSet
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


# 可以将get请求绑定到list方法上 router配置
# goods_list = GoodsListViewset.as_view({
#     'get': 'list'
# })

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewset, basename="goods")
router.register(r'categorys', CategoryViewSet, basename="categorys")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 登陆配置 如果不配置这个看到的api页面就没有登录按钮
    path('api-auth/', include("rest_framework.urls")),
    # 配置媒体文件夹路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}, name='media'),

    # 商品列表页
    # path(r'goods/', GoodsListView.as_view(), name="goods-list"),
    # router配置
    # path(r'goods/', goods_list, name="goods-list"),
    path('', include(router.urls)),
    path('openapi', get_schema_view(title="生鲜电商"), name='openapi-schema'),
    path('api-token-auth/', views.obtain_auth_token),
]
