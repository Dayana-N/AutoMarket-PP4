from listings.models import CarMake, CarModel
from rest_framework import serializers

# Serialize the CarMake and CarModel models


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
