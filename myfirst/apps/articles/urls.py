from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:articles_id>/', views.detail, name='detail'),
    path('<int:articles_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]