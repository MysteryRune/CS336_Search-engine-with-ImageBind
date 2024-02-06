from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_home, name="Home"),
    path("about/", views.index_about, name="About"),
    path("retrieval_result/", views.index_retrieval_result, name="Retrieval Result"),
]