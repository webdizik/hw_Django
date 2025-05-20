# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .serializers import SensorDetailSerializer, MeasurementSerializer
from .models import Sensor, Measurement


class SensorView(ListCreateAPIView):
    
    # получение датчиков
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    
class SensorCreate(CreateAPIView): 
      
    # создание датчика
    def post(self, request):
        return Response (
            { "name": "ESP32", "description": "Датчик у входа"}
        )


class SensorInfo(RetrieveUpdateAPIView):
    # получение информации по датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    # обновление датчика
    def patch(self, request, pk):
        return Response (
            {"description": "Перенес датчик на балкон"}
        )

   
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # добавление измерения датчика
    def post(self, request):
        return Response (
            {"temperature": 22.3, "created_at": "2021-09-22 16:20:00", "sensor": {"id": 1, "name": "ESP32", "description": "Датчик у входа"}}
        )
        