from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from hotsearch.models import HotSearch

def hot_search_list(request):
    hot_searches = HotSearch.objects.all().order_by('-created_at')  # 按创建时间降序排列
    return render(request, 'hotsearch/hot_search_list.html', {'hot_searches': hot_searches})