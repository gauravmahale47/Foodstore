from django.urls import path
from foodapp.views import *
from django.views.generic.base import TemplateView
from .views import FoodCreateView,FoodListView
from django.conf import settings
from django.conf.urls.static import static 
'''
    TemplateView is built-in django Class Based view Class 
    which is used to render the request to template, 
'''
urlpatterns = [
    # FBV
    # path('',index),
    # path('addfood',addfood),
    path('',TemplateView.as_view(template_name='foodapp/index.html'),name="Home"),
    path('addfood',FoodCreateView.as_view(),name='addfood'),
    path('foodlist',FoodListView.as_view(),name='foodmenu'),
    path('foodupdate/<pk>',FoodUpdateView.as_view(),name='foodupdate'),
    path('fooddelete/<pk>',FoodDeleteView.as_view(),name='fooddelete'),
    path('fooddetail/<pk>',FoodDetailView.as_view(),name='fooddetail')
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)