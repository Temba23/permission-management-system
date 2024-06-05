from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Data
from .serializers import DataSerializer
from rest_framework import status

class DataView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DataSerializer

    def get(self, request):
        user = request.user
        data = Data.objects.filter(user=user)
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)









