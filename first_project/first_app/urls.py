from django.urls import path
from . import views

urlpatterns = [
    path("help", views.help, name="help"),
    path('template', views.template, name='template'),
    path("userinfo", views.userinfo, name="users"),
    path("forms", views.form_view, name="form_view"),
    path("index", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.user_logout, name="logout"),
    path("special", views.special, name="special"),
    path("login", views.user_login, name="login"),
]

# TEMPLATE TAGGING

app_name = 'first_app'

