from rest_framework import serializers

from .models import Fias


class FiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fias
        #fields = "__all__"
        fields = ("Houseid", "Houseguid")