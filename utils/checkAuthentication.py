from django.contrib.auth import authenticate
def checkAuth(username,password):
    return authenticate(username=username,password=password)