from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="serachentry"),
    path("add", views.add, name="add"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("random", views.random_page, name="random"),
    path("afteredit", views.afteredit, name="afteredit"),
    path("<str:name>", views.select, name="selectentry")
]
