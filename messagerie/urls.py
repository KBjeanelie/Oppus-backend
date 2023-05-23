from django.urls import path

from messagerie.views import DiscussionDetailView, DiscussionListCreateView
urlpatterns = [
    path('', DiscussionListCreateView.as_view()),
    path('<int:pk>/', DiscussionDetailView.as_view()),
]