from django.shortcuts import render
from rest_framework import generics
from .models import Recipe
from .serializer import RecipeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, filters, viewsets


# Create your views here.
@api_view(['GET', 'POST'])
def show_recipes(request):
    # request_instance = Event.objects.create()
    if request.method == 'GET':
        data = Recipe.objects.all()

        serializer = RecipeSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
