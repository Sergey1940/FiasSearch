from rest_framework import generics, viewsets, filters, status
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .models import Fias
from .serializers import FiasSerializer


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Fias
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Fias.objects.filter(
            Q(Houseid__icontains=query) | Q(
                Houseguid__icontains=query)
        )
        return object_list


# ReadOnlyModelViewSet
# ModelViewSet
class FiasViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset= Fias.objects.all()
    serializer_class = FiasSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        guid = self.kwargs.get("Houseid")

        if not pk:
            return Fias.objects.all()[:1]
        return Fias.objects.filter(pk=pk)


class FiasAPIView(generics.ListAPIView):
    queryset = Fias.objects.all()
    serializer_class = FiasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Houseid', 'Houseguid']

class FiasAPIView2(APIView):
    def post(self, request, format=None):
        query = request.data.get('query')
        print("hello hays")
        if query:
            fiaslist = Fias.objects.filter(Q(Houseid__icontains=query) | Q(Houseguid__icontains=query))
        else:
            fiaslist = Fias.objects.none()
        serializer = FiasSerializer(fiaslist, many=True)
        return Response(serializer.data)

# class FiasAPIView(APIView):
#     def get(self, request):
#         fiaslist = Fias.objects.all()
#         return Response({'posts': FiasSerializer(fiaslist, many=True).data})
#
#     def post(self, request):
#         serializer = FiasSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT now allowed"})
#
#         try:
#             instance = Fias.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT now allowed"})
#
#         serializer = FiasSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
