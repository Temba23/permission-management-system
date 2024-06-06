from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Data
from .serializers import DataSerializer
from rest_framework import status

class DataView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DataSerializer

    def get(self, request, pk=None):
        user = request.user
        if pk:
            try:
                data = Data.objects.get(user=user, id=pk)
                serializer = DataSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Data.DoesNotExist:
                return Response("No data found.", status=status.HTTP_404_NOT_FOUND)
        else:
            data = Data.objects.filter(user=user)
            serializer = self.serializer_class(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        try:
            data = Data.objects.get(id=pk, user=request.user)
            serializer = self.serializer_class(data, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Data.DoesNotExist:
            return Response("Data Doesnot exist.")
        
    def delete(self, request, pk):
        data = Data.objects.get(id=pk, user=request.user)
        try:
            data.delete()
            return Response("Data Deleted Successfully.", status=status.HTTP_200_OK)
        except Data.DoesNotExist:
            return Response("Data Not Found.", status=status.HTTP_404_NOT_FOUND)
            
        