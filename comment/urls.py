from django.urls import path
from .import views

urlpatterns = [

    path('comment/add/news/(?P<pk>\d+)/', views.news_cm_add, name='news_cm_add'),
    path('comments/list/', views.comments_list, name='comments_list'), # Cooments list in Panel
    path('comments/del/(?P<pk>\d+)/', views.comments_del, name='comments_del'), # Cooments delete in Panel
    path('comments/confirm/(?P<pk>\d+)/', views.comments_confirm, name='comments_confirm'), # Cooments Confirm in Panel
]