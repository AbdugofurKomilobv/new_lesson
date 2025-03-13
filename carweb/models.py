from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=120)
    prise = models.IntegerField()
    more = models.TextField(blank=False)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "CAR"
        verbose_name_plural = "CARS"
        ordering = ['created_ed']

