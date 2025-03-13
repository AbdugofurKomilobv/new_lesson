from django.urls import path

from common.views import home_page,category_news

urlpatterns = [
      path('',home_page,name='home'),
      path('category/<int:category_id>/',category_news)
]