from django.conf.urls import url
from first_app import views

#template tagging
app_name = 'first_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^crearcuenta/$',views.crearcuenta,name='crearcuenta'),
    url(r'^inicio/$',views.inicio,name='inicio'),
    url(r'^$',views.index,name='index'),
    url(r'^$',views.usuarios,name='users'),
]
