from django.urls import path
from .views import home_page, category_page, news_detail
from . import views

urlpatterns = [
    path('', home_page, name='home'),
    path('category/<int:pk>/', category_page, name='category_page'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('register', views.Register.as_view()),
    path('search', views.search_product)
]

