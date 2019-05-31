from question import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('post/',views.post,name='post'), #글쓰기
    path('<int:board_id>/',views.detail,name='detail'), # 글 상세보기 
    path('show/',views.show,name='show'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete,name='delete'),
] 

