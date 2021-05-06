from django.shortcuts import render
from .models import(
    Todoitem
)
from .serializer import(
    TodoitemSerializer
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes

# Create your views here.


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@parser_classes([JSONParser])
def itemslist(request):

    items = Todoitem.objects.filter(user=request.user)
    serializer = TodoitemSerializer(items, many=True)
    return Response(serializer.data,status=200)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@parser_classes([JSONParser])
def create(request):

    data = request.data
    data['user']=request.user.id
    serializer = TodoitemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
                'status':'added'
            },status=201)

    return Response({
                'status':'failed',
                'message':serializer.errors
            },status=400)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@parser_classes([JSONParser])
def delete(request,pk):

    try:
        item = Todoitem.objects.get(id=pk)
        item.delete()
        return Response(status=202)
    except:
        return Response(status=404)
