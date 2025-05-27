from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('matching/', views.matching_view, name='matching'),
    path('community/', views.community, name='community'),
    path('content/', views.content, name='content'),
    path('company/', views.company, name='company'),
    path('custom/', views.custom, name='custom'),
    path('price/', views.price, name='price'),
    path('shop-detail1/', views.shopdetail1, name='shopdeatail1'),
    path('shop-detail2/', views.shopdetail2, name='shopdeatail2'),
    path('shop-detail3/', views.shopdetail3, name='shopdeatail3'),
    path('shop-detail4/', views.shopdetail4, name='shopdeatail4'),
    path('fashionista/', views.fashionista, name='fashionista'),
    path('supernova/', views.supernova, name='superrnova'),
    path('content/colortone.html', views.colortone, name='colortone'),
    path('content/poweroutfit.html', views.poweroutfit, name='poweroutfit'),
    path('content/gogreener.html', views.gogreener, name='gogreener'),
    path('content/diy.html', views.diy, name='diy'),
]