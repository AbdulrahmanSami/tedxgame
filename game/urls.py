from django.conf.urls import include, url
from . import views
urlpatterns = [
    url("^$", views.handle_index, name="handle_index"),
    url("^handle_ajax/$", views.handle_ajax, name="handle_ajax"),
    #url("^choose$", views.choose, name="choose"),
]