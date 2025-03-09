from django.db import models

# Create your models here.
class hot_search(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    num = models.CharField(max_length=100)
    title = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.num
