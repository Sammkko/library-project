from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('adt', views.adt, name='adt'),
    path('catalogs', views.catalogs, name='catalogs'),
    path('collection', views.collection, name='collection'),
    path('contact', views.contact, name='contact'),
    path('structure', views.structure, name='structure'),
    path('photo', views.photo, name='photo'),
    path('mission', views.mission, name='mission'),
    path('video', views.video, name='video'),
    path('history', views.video, name='history'),
    path('vacancy', views.video, name='vacancy'),
    
    path('photoOnly/<str:pk>', views.photoOnly, name='photo-Only'),
    path('videoOnly', views.videoOnly, name='videoOnly'),
]
# login adminlib
# password adminadmin