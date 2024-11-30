from django.urls import path
from .views import CreateUserView, LoginView, LogoutView

urlpatterns = [
    path('user/signup/', CreateUserView.as_view(), name='signup'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
]
