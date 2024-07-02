# urls.py
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add_post/', views.add_post, name='add_post'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout_user')
]
