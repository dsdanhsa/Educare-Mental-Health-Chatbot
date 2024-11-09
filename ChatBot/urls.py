from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chatbot_home'),
    path('get/', views.get_bot_response, name='get_bot_response'),  
]