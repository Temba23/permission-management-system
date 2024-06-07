from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Data
from .serializers import DataSerializer
from rest_framework import status
from django.db.models import Q

class DataView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DataSerializer

    def get(self, request, pk=None):
        user = request.user
        role = user.role
        
        if pk:    
            if role in ["admin", "staff"]:
                try: 
                    data = Data.objects.get(id=pk)
                    serializer = DataSerializer(data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Data.DoesNotExist:
                    return Response("No data found.", status=status.HTTP_404_NOT_FOUND)
            else:
                try: 
                    data = Data.objects.get(user=user, id=pk)
                    serializer = DataSerializer(data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Data.DoesNotExist:
                    return Response("No data found.", status=status.HTTP_404_NOT_FOUND)
        else:
            if role in ["admin", "staff"]:
                data = Data.objects.all()
                serializer = self.serializer_class(data, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                data = Data.objects.filter(user=user).all()
                serializer = self.serializer_class(data, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        user = request.user
        data = Data.objects.get(id=pk)
        if data.user == user or user.role == "admin":
            try:
                serializer = self.serializer_class(data, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Data.DoesNotExist:
                return Response("Data Doesnot exist.")
        else:
            return Response({"Error" : "You don't have the access."})
        
    def delete(self, request, pk):
        user=request.user
        role = request.user.role
        try:            
            if role == "admin":
                data = Data.objects.get(id=pk)
            else:
                data = Data.objects.get(id=pk, user=user)        
            data.delete()
            return Response("Data Deleted Successfully.", status=status.HTTP_200_OK)
        
        except Data.DoesNotExist:
            return Response("Data Not Found.", status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)   