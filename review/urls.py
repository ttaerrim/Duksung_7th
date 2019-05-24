from review import views
from django.urls import path

urlpattern = [
    path('rpost/', views.rpost, name = 'rpost'),
    #paht('<int:review_id)/', views.rdetail, name='rdetail'),
    path('rmain/', views.rmain, name='rmain'),
    path('<int:pk>/redit/', views.redit, name='redit'),
]