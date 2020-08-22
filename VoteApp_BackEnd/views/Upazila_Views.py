from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Upazila
from ..serializers import UpazilaSerializer


@api_view(['GET', 'POST'])
def upazila_listCreate(request):
    """
    List all code upazilas, or create a new upazila.
    """
    if request.method == 'GET':
        upazilas = Upazila.objects.all()
        serializer = UpazilaSerializer(upazilas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UpazilaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def upazila_detail(request, id):
    """
    Retrieve, update or delete a code upazila.
    """
    try:
        upazila = Upazila.objects.get(id=id)
    except Upazila.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpazilaSerializer(upazila)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpazilaSerializer(upazila, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        upazila.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)