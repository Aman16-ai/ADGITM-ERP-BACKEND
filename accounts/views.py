from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FacultySerializer
from utils.generateJWT import generate
# Create your views here.
class registerFacultyView(generics.CreateAPIView):
    serializer_class = FacultySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print("user --> ",user)
            if user is not None:
                return Response({"status":"success","token":generate(user)},status=201)
            
        else:
            return Response({"status":"failed",},status=400)