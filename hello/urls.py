from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("roman", views.roman, name="roman"),
    # a generic path for our greet function
    path("<str:name>", views.greet, name="greet")
]
