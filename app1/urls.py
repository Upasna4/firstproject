from app1 import views
from django.conf.urls import url

app_name = 'app1'

urlpatterns=[
    url(r'about/$',views.about,name="about")
]