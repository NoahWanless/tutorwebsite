from django.urls import path
from .views import HomePageView, TutorDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tutors/<int:pk>/", TutorDetailView.as_view(), name="tutor_detail"),
]
