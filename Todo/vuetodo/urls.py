from django.urls import re_path
from vuetodo import views

urlpatterns = [
    re_path(r'^$', views.VueTodo, name='vuetodo'),

    re_path(r'^redisstorage$', views.VueTodo),
]
