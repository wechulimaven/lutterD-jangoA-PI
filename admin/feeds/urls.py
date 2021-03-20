from django.urls import path
from .views import UserRecordView, feedEditAddPostList, feedPostsList


urlpatterns = [
    path('', feedPostsList.as_view()),
    path('<int:pk>/', feedEditAddPostList.as_view()),
    path('user/', UserRecordView.as_view(), name='users'),

    ]