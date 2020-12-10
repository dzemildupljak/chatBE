from django.urls import path
from chat_api import views

urlpatterns = [
    # path('', views.getAllMessages),
    path('users/', views.get_all_users),
    path('message-list/<int:sender>/<int:receiver>', views.get_all_messages),
    path('message/', views.create_messages)
]