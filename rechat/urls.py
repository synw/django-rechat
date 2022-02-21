from django.urls import path

from rechat.views import ChatView, PostView, RoomsListView, ChatIndexView


urlpatterns = [
    path("room/<str:room>/", ChatView.as_view(), name="rechat-room"),
    path("post/<str:room>/", PostView.as_view(), name="rechat-post"),
    path("rooms/", RoomsListView.as_view(), name="rechat-rooms"),
    path("", ChatIndexView.as_view()),
]
