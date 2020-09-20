from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view(), name='create'),
    path('token/', views.CreateTokenAPIView.as_view(), name='token'),
    path('profile/', views.UpdateRetriveUserAPIView, name='profile')
]