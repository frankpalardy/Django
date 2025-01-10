from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from .models import Item
from .serializers import UserRegistrationSerializer, ItemSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = UserRegistrationSerializer()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

def test_view(request):
    return render(request, 'test.html')