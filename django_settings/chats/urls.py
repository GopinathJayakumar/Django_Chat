
from django.urls import path

from .views import chat_details_view, chat_list_view

urlpatterns = [
    path('', chat_list_view, name='list'),
    path('1/', chat_details_view, name='detail'),
]