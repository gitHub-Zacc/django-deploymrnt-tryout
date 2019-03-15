from django.urls import path
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    # path('help/', views.help, name="help"),
    path('users/', views.users, name="users"),
    path('user_login/', views.user_login, name='user_login'),
]
