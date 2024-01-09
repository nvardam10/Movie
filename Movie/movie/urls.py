from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 
# from movie.views import *
urlpatterns = [
    path('register',UserRegisterView.as_view()),
    path('register/<int:UserID>/', UserDetailedView.as_view()),

    path('login',UserLoginView.as_view()),
    path('login/<int:pk>/',UserLoginView.as_view()),

    path('list',MovieListView.as_view()),
    path('list/<int:MovieID>/', MovieDetailedView.as_view()),

    path('booking',BookingView.as_view()),
    path('booking/<int:BookingID>/', BookingDetailedView.as_view()),

    path('login-user/', login_user),

    path('gettoken/',TokenObtainPairView.as_view(), name='token_obatin_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(), name='token_verify')
    
 ]