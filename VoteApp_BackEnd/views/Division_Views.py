from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Division
from ..serializers import DivisionSerializer


@api_view(['GET', 'POST'])
def division_listCreate(request):
    """
    List all code divisions, or create a new division.
    """
    if request.method == 'GET':
        divisions = Division.objects.all()
        serializer = DivisionSerializer(divisions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def division_detail(request, id):
    """
    Retrieve, update or delete a code division.
    """
    try:
        division = Division.objects.get(id=id)
    except Division.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DivisionSerializer(division)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DivisionSerializer(division, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        division.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)