from django.urls import path
from . import views

urlpatterns = [
    path('', views.hot_search_list, name='hot_search_list'),  # 热搜列表视图
]