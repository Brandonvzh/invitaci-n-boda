from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Guests
from .serializers import GuestsAPI

class GuestsAutoViewSet(viewsets.ModelViewSet):
    serializer_class = GuestsAPI
    filterset_fields = ('identifier')
    queryset = Guests.objects.all()

@api_view(['GET'])
def get_guests_data(request, data):
    queryset = Guests.objects.filter(code = str(data))
    
    if queryset:
        if request.method == 'GET':
            serializer = GuestsAPI(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
    elif not queryset:
        return Response({"error": "No se encontraron registros para el mes dado."}, status=status.HTTP_404_NOT_FOUND)

