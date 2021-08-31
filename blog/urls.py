# blog/urls.py
# http://127.0.0.1:8000/blog/   : 블로그 리스트 페이지
# http://127.0.0.1:8000/blog/1  : 1번 글 상세보기 페이지

from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail')
#    path('', views.index),
#    path('<int:pk>/', views.detail, name='detail'),
]
