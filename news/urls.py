from django.urls import path
from .import views

urlpatterns = [

    path('news/(?P<word>.*)/', views.news_detail, name='news_detail'),       ## Front News Details Page   
    path('panel/news/list/', views.news_list, name='news_list'),             ## Admin Panel News List
    path('panel/news/add/', views.news_add, name='news_add'),                 ## Admin Panel Add News      
    path('panel/news/del/(?P<pk>\d+)/', views.news_delete, name='news_delete'),   ## Admin Panel Delete News
    path('panel/news/edit/(?P<pk>\d+)/', views.news_edit, name='news_edit'),    ## Admin Panel Edit News
    path('panel/news/publish/(?P<pk>\d+)/', views.news_publish, name='news_publish'),   ## Admin Panel Publish News   
    path('urls/(?P<pk>\d+)/', views.news_detail_short, name='news_detail_short'),       ## Front News Short Url  
]                                                                               






# # word is a variable and d means digit. w means digit or number
# # used P for received the value as a Parenthesis