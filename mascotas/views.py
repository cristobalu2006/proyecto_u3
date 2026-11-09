from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mascotas.models import Responsable
from mascotas.models import Mascota


from mascotas.serializers import ResponsableSerializer
from mascotas.serializers import MascotaSerializer


@api_view(['POST', 'PUT']) #FUNCIONA
def crear_mascota(request):
    mascota_deserializado = MascotaSerializer(data=request.data)

    if mascota_deserializado.is_valid():
        mascota_deserializado.save()
        return Response(mascota_deserializado.errors, status=status.HTTP_201_CREATED)
    else:
        return Response(mascota_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET']) #FUNCIONA
def listar_mascotas(request):
    try:
        listado_mascotas = Mascota.objects.all()
        serializado = MascotaSerializer(listado_mascotas, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def modificar_mascotas(request, id):
    try:
        mascota_obtenida = Mascota.objects.get(id=id)
        serializado = MascotaSerializer(mascota_obtenida, data=request.data)

        if serializado.is_valid():
            serializado.save()

            return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def eliminar_mascotas(request, id):
    try:
        mascota_obtenida = Mascota.objects.get(id=id)
        mascota_obtenida.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NO_CONTENT)









@api_view(['POST', 'PUT']) #FUNCIONA
def crear_responsable(request):
    responsable_deserializado = ResponsableSerializer(data=request.data)

    if responsable_deserializado.is_valid():
        responsable_deserializado.save()
        return Response(responsable_deserializado.errors, status=status.HTTP_201_CREATED)
    else:
        return Response(responsable_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) #FUNCIONA
def listar_responsables(request):
    try:
        listado_responsables = Responsable.objects.all()
        serializado = ResponsableSerializer(listado_responsables, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def modificar_responsable(request, id):
    try:
        responsable_obtenido = Responsable.objects.get(id=id)
        serializado = ResponsableSerializer(responsable_obtenido, data=request.data)

        if serializado.is_valid():
            serializado.save()

            return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def eliminar_responsable(request, id):
    try:
        responsable_obtenido = Responsable.objects.get(id=id)
        responsable_obtenido.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NO_CONTENT)
