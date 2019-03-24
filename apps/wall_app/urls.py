from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete$', views.delete)
]