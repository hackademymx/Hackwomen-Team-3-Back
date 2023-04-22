from django.urls import URLPattern, path
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView


urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view())
]