from django.urls import path
from .views import CreateUserView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    # Django Auth system
    # path('user/signup/', CreateUserView.as_view(), name='signup'),
    # path('user/login/', LoginView.as_view(), name='login'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),

    path('user/login/', TokenObtainPairView.as_view(), name='login'),
]

