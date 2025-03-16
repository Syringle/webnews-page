from django.urls import path
from .views import home_page, category_page, news_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('category/<int:pk>/', category_page, name='category_page'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
]
