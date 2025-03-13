from django.db import models


class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=100)


    def __str__(self):
        return self.title_name

    class Meta:
        verbose_name = 'CATEGORY'
        verbose_name_plural = 'CATEGORYS'


class News(models.Model):
    title = models.CharField(max_length=150)
    context = models.TextField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "NEW"
        verbose_name_plural = "NEWS"
        ordering = ['created_ed']


