from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import FacultySerializer,LoginSerializer,UserAccountSerializer,GetFacultySerializer
from .models import Faculty,UserAccount
from middleware.custom_premission import HigherAuthoritiesPremission
from utils.generateJWT import generate
from utils.checkAuthentication import checkAuth
from rest_framework import status
# Create your views here.
class registerFacultyView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    # serializer_class = FacultySerializer
    permission_classes = [HigherAuthoritiesPremission]

    serializers = {
        'GET':    GetFacultySerializer,
        'POST': FacultySerializer
        # etc.
    }
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializers['GET']
        return self.serializers['POST']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print("user --> ",user)
            if user is not None:               
                return Response({"status":"success","token":generate(user)},status=201)
            
        else:
            return Response({"status":"failed",},status=400)
        

class userView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        if user is not None:
            if user.role == 'HOD' or user.role == 'DI' or user.role == 'Assistant Professor' or user.role == 'professor':
                fac = Faculty.objects.get(faculty_user = user)
                fac_ser = FacultySerializer(fac)
                return Response({'status': status.HTTP_200_OK,"Response":fac_ser.data},status=status.HTTP_200_OK)
            else:
                return Response({'status': status.HTTP_200_OK,'Response':UserAccountSerializer(user).data},status=status.HTTP_200_OK)
        return Response({"message":"user not found"},status=400)
    

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        # login_ser = LoginSerializer(data = request.data)
        login_ser = self.get_serializer(data = request.data)
        if login_ser.is_valid(raise_exception=True):
            username = login_ser.data['username']
            password = login_ser.data['password']
            user = checkAuth(username=username,password=password)
            print('user ------> ',user)
            if user is not None:
                token = generate(user=user)
                return Response({"status":status.HTTP_201_CREATED,"Response":token},status=201) 
        
        return Response({"Error":"Login Failed"})
    

class registerUser(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [HigherAuthoritiesPremission]

    # todo : generate token also same as register facult
    
        
    