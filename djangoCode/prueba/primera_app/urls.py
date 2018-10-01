from django.conf.urls import url
from primera_app import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]
