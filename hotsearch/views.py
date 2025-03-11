from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from hotsearch.models import HotSearch

def hot_search_list(request):
    """
    展示微博热搜榜的视图
    """
    # 从数据库中获取所有热搜数据
    hot_searches = HotSearch.objects.all().order_by('id')  # id前加-决定倒序（按照最新排序）
    context = {
        'hot_searches': hot_searches
    }
    return render(request, 'hotsearch/hot_search_list.html', context)