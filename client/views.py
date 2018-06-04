from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from client.models import *
from client.serializers import *

@csrf_exempt
def library(request, name):
    """
    Returns a single library matching the name constraint, or creates a version for the library specified.
    """

    if request.method == 'GET':
        try:
                library = Library.objects.get(name=name)
                serializer = LibrarySerializer(library)
                return JsonResponse(serializer.data)
        except Library.DoesNotExist:
                data = {}
                data['status'] = '404'
                data['content'] = str('Could not find any libraries called "%s"' % (name))
                return JsonResponse(data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if 'library_id' not in data:
            related_library = Library.objects.get(name=name)
            data['library_id'] = related_library.id
        serializer = VersionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def libraries(request):
    """
    Returns all libraries, or creates a new library.
    """

    if request.method == 'GET':
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def library_version(request, name, version_string):
    """
    Retrieves a library based on version.
    """

    if request.method == 'GET':
        try:
            try:
                related_library = Library.objects.get(name=name)
            except Library.DoesNotExist:
                data = {}
                data['status'] = '404'
                data['content'] = str('Could not find a library called "%s"' % (name))

            library_version = Version.objects.get(library_id=related_library.id, version=version_string)
            serializer = VersionSerializer(library_version)
            return JsonResponse(serializer.data)
        except Version.DoesNotExist:
                data = {}
                data['status'] = '404'
                data['content'] = str('Could not find version %s for a library called "%s"' % (version_string, name))

        return JsonResponse(data)

@csrf_exempt
def library_resource(request, name, version):
    """
    Adds or views a resource for a specified version of a library.
    """

    if request.method == 'GET':
        try:
            library = Library.objects.get(name=name)
        except Library.DoesNotExist:
            data = {}
            data['status'] = '404'
            data['content'] = str('Could not find any libraries called "%s"' % (name))
            return JsonResponse(data)

        try:
            library_version = Version.objects.get(name=name, version=version)
        except Version.DoesNotExist:
            data = {}
            data['status'] = '404'
            data['content'] = str('Could not find version %s for a library called "%s"' % (version, name))
            return JsonResponse(data)

        try:
            library_resource = Resource.objects.get(version=library_version)
        except Resource.DoesNotExist:
            data = {}
            data['status'] = '404'
            data['content'] = str('Could not find a resource for version %s of library "%s"' % (version, name))
            return JsonResponse(data)

        serializer = ResourceSerializer(library_resource, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResourceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
