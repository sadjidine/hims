from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import Category, Speciality, Codification, Pathology, Nomenclature, Medication, Agreement, CareService, \
    Practitioner, HealthCenter, CareItem, CareOnDemand, MedicationItem, HealthCare

from .serializers import CategorySerializer, SpecialitySerializer, CodificationSerializer, PathologySerializer, \
    NomenclatureSerializer, MedicationSerializer, AgreementSerializer, CareServiceSerializer, PractionerSerializer, \
    HealthCenterSerializer, CareItemSerializer, CareOnDemandSerializer, MedicationItemSerializer, HealthCareSerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Codification.objects.filter(category_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Category cannot be deleted because it have attached codifications.'})
        return super().destroy(request, **args, **kwargs)


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Pathology.objects.filter(speciality_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Speciality cannot be deleted because it have attached pathologies.'})
        return super().destroy(request, **args, **kwargs)
    # def delete(self, request, pk):
    #     speciality = get_object_or_404(Speciality, pk=pk)
    #     if speciality.pathologies.count() > 0:
    #         return Response({'error': 'Speciality cannot be deleted because it have attached pathologies.'})
    #     speciality.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CodificationViewSet(ModelViewSet):
    queryset = Codification.objects.all()
    serializer_class = CodificationSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Nomenclature.objects.filter(codification_id=kwargs['pk']).count() > 0:
            return Response({'error': 'This codification cannot be deleted because it have attached nomenclature.'})
        return super().destroy(request, *args, **kwargs)
