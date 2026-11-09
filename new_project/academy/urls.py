from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.course_list, name="courses"),
    path("courses/<slug:slug>/", views.course_detail, name="course_detail"),
    path("contact/", views.contact, name="contact"),
]
