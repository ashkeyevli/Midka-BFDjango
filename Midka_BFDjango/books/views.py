from django.shortcuts import render
from django.shortcuts import render
from .models import BookJournalBase, Book, Journal
from auth_.models import MainUser
from rest_framework import generics, mixins, viewsets
from books.serializers import BookJournalBaseSerializer, BookSerializer, JounralSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.constants import USER_ROLE_SUPERUSER
# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    # permission_classes = (MainUser.role == USER_ROLE_SUPERUSER)
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    @action(methods=['PUT'], detail=False, permission_classes = (MainUser.role == USER_ROLE_SUPERUSER) )
    def edit(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    @action(methods=['DELETE'], detail=False, permission_classes = (MainUser.role == USER_ROLE_SUPERUSER) )
    def edit(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

class JournalViewSet(viewsets.ModelViewSet):
    # permission_classes = (MainUser.role == USER_ROLE_SUPERUSER)
    serializer_class = JounralSerializer
    queryset = Journal.objects.all()
    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    @action(methods=['PUT'], detail=False, permission_classes = (MainUser.role == USER_ROLE_SUPERUSER) )
    def edit(self, request):
        queryset = Journal.objects.all()
        serializer = JounralSerializer(queryset)
        return Response(serializer.data)
    @action(methods=['DELETE'], detail=False, permission_classes = (MainUser.role == USER_ROLE_SUPERUSER) )
    def edit(self, request):
        queryset = Journal.objects.all()
        serializer = JounralSerializer(queryset)
        return Response(serializer.data)