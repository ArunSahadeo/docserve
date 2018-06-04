from rest_framework import serializers
from client.models import Library, Version, Resource

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'language')

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('library_id', 'version')

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('repoREADME', 'websiteLanding', 'websiteDocs')
