from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Data
from .serializers import DataSerializer
from rest_framework import status
from django.db.models import Q
from authentication.models import CustomUser

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
        
class ChangeRole(APIView):
    def get(self, request):
        return Response("No GET method.", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def post(self, request):
        for required in ['id', 'desired_role']:
            if request.data.get(required) is None:
                return Response({"message": f'Please send the {required} along with request.'}, status=status.HTTP_400_BAD_REQUEST)
            
        user_role = request.user.role
        pk = request.data.get('id')
        desired_role = request.data.get('desired_role')
        print("User role: ",user_role)
        if user_role == "admin":
            if desired_role in ['admin', 'staff', 'user']:
                try:
                    user = CustomUser.objects.get(id=pk)
                    user.role = desired_role
                    user.save()
                    return Response("Role changed.", status=status.HTTP_200_OK)
                except CustomUser.DoesNotExist:
                    return Response("User doesnot exist.", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Invalid Role.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Don't Have This Access.", status=status.HTTP_403_FORBIDDEN)