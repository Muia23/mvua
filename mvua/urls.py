from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.HomeAPIView.as_view()),
]