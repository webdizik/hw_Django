from django.urls import path
from .views import SensorView, SensorCreate, SensorInfo, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorInfo.as_view()),
    path('sensor/', SensorCreate.as_view()),
    path('sensor/<pk>/', SensorInfo.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
