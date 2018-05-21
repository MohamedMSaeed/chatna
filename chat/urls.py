from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list



    # ex: /chat/signup
    path('signup/', views.Signup.as_view(), name='signup'),
    # /chat/logout
    path('logout/', auth_views.logout, name='logged_out'),
    # /chat/login
    path('login/', auth_views.login, name='login'),
]
