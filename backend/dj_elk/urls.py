from django.urls import path, include

urlpatterns = [
    path('rest/', include('apps.rest.urls')),
]
