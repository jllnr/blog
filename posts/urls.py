from django.contrib import admin
from django.urls import path, re_path
from posts import views as post_view
from . import views

urlpatterns = [
    path('', views.post_list, name="list"),
    path('create/', views.post_create),
    #path('detail/(?P<title>\d+)/', views.post_detail),
    #path('<title:id>/', views.post_detail),
    #re_path('detail/(?P<id>\d+)/', views.post_detail),
    re_path('(?P<id>\d+)/', views.post_detail),
    #re_path('(?P<id>\d+)/edit/', views.post_update, name="update"),
    #re_path('update/(?P<id>\d+)/', views.post_update, name="update"),
    #path('<str:slug>/edit/', views.post_update, name="update"),
    #path('update/', views.post_update, name="update"),
    #re_path('(?P<id>\d+/update/', views.post_update, name="update"),
    #re_path('update/(?P<id>\d+)/', views.post_update, name="update"),
    #path('(?P<id>\d+)/delete/', views.post_delete),
    path('update/<int:id>/', views.post_update, name="update"),
    path('<int:id>/delete/', views.post_delete)
]
