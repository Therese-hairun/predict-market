from rest_framework import serializers
from .models import Asset, Symbol, Training


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["assetname", "assetfullname"]


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"
