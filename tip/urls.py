from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('post/',views.post,name='post'),
    path('detail/',views.detail,name='detail'),
    path('show/',views.show,name='show'),
    path('<int:tip_id>/',views.detail,name='detail'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('download/<int:pk>',views.download,name='download'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)