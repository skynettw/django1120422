from django.contrib import admin
from django.urls import path
from mysite import views  #去mysite資料夾中匯入views.py這個檔案

urlpatterns = [
    path('', views.index),
    path('lotto/', views.lotto),
    path('lucky/', views.lucky),
    path('admin/', admin.site.urls),
]
