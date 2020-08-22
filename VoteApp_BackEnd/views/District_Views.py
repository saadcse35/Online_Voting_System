from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import District
from ..serializers import DistrictSerializer


@api_view(['GET', 'POST'])
def district_listCreate(request):
    """
    List all code districts, or create a new district.
    """
    if request.method == 'GET':
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def district_detail(request, id):
    """
    Retrieve, update or delete a code district.
    """
    try:
        district = District.objects.get(id=id)
    except District.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DistrictSerializer(district)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DistrictSerializer(district, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)