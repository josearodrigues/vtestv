from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login-usuario/', views.user_login, name='user_login'),
    path('logout-usuario/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.change_password, name='change_password'),
]