from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from account.models import *
from .serializers import *

class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'data':serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status':False,
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)