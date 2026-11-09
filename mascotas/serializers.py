from rest_framework import serializers

from mascotas.models import Responsable
from mascotas.models import Mascota

#Un serializador es una clase que permite transformnar json a objetos y al revés 
class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'