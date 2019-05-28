from django.urls import path
from review import views

urlpatterns= [
    path('rmain/', views.rmain, name='rmain'), # 후기 메인
    path('redit/', views.redit, name='redit'), # 후기 글수정
    path('rpost/', views.rpost, name='rpost'), # 후기 글쓰기
]
    
  