from rest_framework import serializers
from .models import Knigi
from .models import Clen

class KnigiSerializer(serializers.Serializer):
    class Meta:
        model = Knigi
        fields = "__all__"
        read_only_fields = ('pozajmena_kniga')

    def create(self, validated_data):
        return Knigi.objects.create(**validated_data)

class ClenSerializer(serializers.ModelSerializer):
    naslov_kniga = serializers.SerializerMethodField()

    class Meta:
        model = Clen
        fields = "__all__"

    def create(self, validated_data):
        return Clen.objects.create(**validated_data)
    
    def get_naslov_kniga(self, obj):
        return obj.pozajmena_kniga.naslov

    def get_naslov_kniga(self, obj):
        if obj.pozajmena_kniga != None:
            return obj.pozajmena_kniga.naslov
        else:
            return "Nema pozajmeno"