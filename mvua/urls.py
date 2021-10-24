from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.HomeAPIView.as_view()),    
    url(r'^chart$', views.ChartAPIView.as_view()),    
    url(r'^home$', views.home, name='home'),
]