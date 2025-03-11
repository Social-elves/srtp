from django.db import models

# Create your models here.
class HotSearch(models.Model):
    keyword = models.CharField(max_length=200)  # 热搜关键词
    link = models.URLField(blank=True, null=True)  # 链接（可以为空）
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.keyword
