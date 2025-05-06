# from django.urls import path
# from . import views

# urlpatterns = [
#     path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from matcher import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
#     path('', views.home, name='home'),  # ✅ เพิ่มบรรทัดนี้
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
#     path('clothing/', views.clothing_list_view, name='clothing_list'),
#     path('clothing/<int:item_id>/', views.clothing_detail_view, name='clothing_detail'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
#     path('clothing/', views.clothing_list_view, name='clothing_list'),
#     path('clothing/<int:item_id>/', views.clothing_detail_view, name='clothing_detail'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
#     path('clothing/', views.clothing_list_view, name='clothing_list'),
#     path('clothing/<int:item_id>/', views.clothing_detail_view, name='clothing_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('outfit-matcher/', views.outfit_matcher_view, name='outfit_matcher'),
    path('clothing/', views.clothing_list_view, name='clothing_list'),
    path('clothing/<int:item_id>/', views.clothing_detail_view, name='clothing_detail'),
]