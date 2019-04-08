# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('search/<str:query>/', views.SearchView, name='search'),
    path('<int:product_id>/result/', views.ResultView, name='result'),
    path('<int:product_id>/save/<int:substitute_id>',
         views.SaveView, name='save'),
    path('<int:product_id>/detail/', views.DetailView, name='detail'),
    path('myproducts/', views.MyProductsView, name='myproducts'),
    path('legal/', views.LegalView, name='legal'),
]
