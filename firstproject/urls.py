"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^home/$',views.home),
    url(r'^user/',include('app1.urls')),
    url(r'^testhome/$',views.testhome),
    url(r'^signup/$',views.signup),
    url(r'^userrole/$',views.userrole),
    url(r'^viewdata/$',views.datafetch),
    url(r'^img/$',views.userimage),
    url(r'^update/$',views.update),
    url(r'^deletedata/$',views.deletedata),
    url(r'^datafetchup/$',views.datafetchup),
    url(r'^fetchimg/$',views.imgdetfetch),
    url(r'^imagefetch/$',views.imagefetch)



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#127.0.0.1:8000

#127.0.0.1