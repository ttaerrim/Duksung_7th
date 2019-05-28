from review import views
from django.urls import path

urlpattern = [
    path('rpost/', views.rpost, name = 'rpost'), # 후기 글수정
    #paht('<int:review_id)/', views.rdetail, name='rdetail'),
    path('rmain/', views.rmain, name='rmain'), # 후기 메인
    path('<int:pk>/redit/', views.redit, name='redit'), # 후기 글쓰기
]
