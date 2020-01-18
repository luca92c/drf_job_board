from django.urls import path
from jobs.views import JobOfferAPIView, JobOfferDetailAPIView

urlpatterns = [
    path('jobs',
         JobOfferAPIView.as_view(),
         name="job-offers-list"),

    path('jobs/<int:pk>',
         JobOfferDetailAPIView.as_view(),
         name="job-offer-detail"),

]