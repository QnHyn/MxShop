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
from django.urls import path, re_path
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views_base import GoodsListView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 配置媒体文件夹路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}, name='media'),

    # 商品列表页
    path(r'goods/', GoodsListView.as_view(), name="goods-list")
]
