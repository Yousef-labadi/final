from django.urls import path
from . import views
urlpatterns = [
    path('',views.form),
    path('registration',views.reg),
    path('login',views.login),
    path('success',views.success),
    path('add-message',views.wall),  
]
