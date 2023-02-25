from django.urls import path
from users.views import SignupView, MyPasswordChangeView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pch/', MyPasswordChangeView.as_view(), name='pch'),
]
