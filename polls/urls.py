# polls/urls.py

from django.urls import path
from .import views

app_name = 'polls'  # This is to define a namespace for URLs

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # Use the class-based view
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
