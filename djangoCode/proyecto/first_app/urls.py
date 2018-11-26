from django.conf.urls import url
from first_app import views

#template tagging
app_name = 'first_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^crearcuenta/$',views.crearcuenta,name='crearcuenta'),
    url(r'^reservacion/$',views.reservacion,name='reservacion'),
    url(r'^inicio/$',views.inicio,name='inicio'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^$',views.index,name='index'),
    url(r'^$',views.usuarios,name='users'),
    # url(r'^asiento/$',views.reservacion, name='asientos'),
    # url(r'^cambio/$', views.cambio, name='cambio'),
]
