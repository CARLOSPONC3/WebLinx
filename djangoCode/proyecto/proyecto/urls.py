"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from first_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^first_app/',include('first_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^special/', views.special,name='special'),
    url(r'^crearcuenta/$',views.crearcuenta,name='crearcuenta'),
    url(r'^reservacion/$',views.reservacion,name='reservacion'),
    url(r'^inicio/$',views.inicio,name='inicio'),
    url(r'^user_login/$',views.user_login,name='user_login'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
