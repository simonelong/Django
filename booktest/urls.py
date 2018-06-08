from django.conf.urls import url
import views
from django.conf.urls import url
import views


urlpatterns =[
    url(r'^$',views.index),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^area/$',views.area),
    url(r'^sheng/(\d+)/$',views.sheng),
    url(r'^shi/$',views.shi),
    url(r'^qu/$',views.qu),
]