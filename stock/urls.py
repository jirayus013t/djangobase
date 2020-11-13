from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('mplaces', views.mplaces, name='mplaces'),
    path('mcreatures', views.mcreatures, name='mcreatures'),
    path('maliens', views.maliens, name='maliens'),
    path('time', views.time, name='time'),

]