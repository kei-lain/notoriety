from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from .serializers import NoteSerializer
from .models import Note
# Create your views here.


class Notesviewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
