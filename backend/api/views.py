from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

class Users(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        output = [{"id": output.id , "username": output.username, "email": output.email} for output in User.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, *args, **kwargs):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'