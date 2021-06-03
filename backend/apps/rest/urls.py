from django.urls import path

from .resources.views import RestAPIView

urlpatterns = [
    path('', RestAPIView.as_view()),
]

