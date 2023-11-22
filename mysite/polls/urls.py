from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # e.g. http://127.0.0.1:8000/polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # e.g. http://127.0.0.1:8000/polls/specifics/1/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # e.g. http://127.0.0.1:8000/polls/1/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),  # e.g. http://127.0.0.1:8000/polls/1/vote/
]