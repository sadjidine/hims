from rest_frameworks import serializers
from medical.models import Category, Speciality, Codification, Pathology, \
    Nomenclature, Molecule, MedicationType, TherapeuticRoute, Medication, \
    CenterType, HealthCenter, Agreement, CareService, Practitioner, HealthCare, CareItem, CareOnDemand, MedicationItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'name')


class CodificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codification
        fields = '__all__'


class PathologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathology
        fields = '__all__'


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class CareServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareService
        fields = '__all__'


class PractionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = '__all__'


class HealthCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCenter
        fields = '__all__'


class CareItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareItem
        fields = '__all__'


class CareOnDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareOnDemand
        fields = '__all__'


class MedicationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationItem
        fields = '__all__'


class HealthCareSerializer(serializers.ModelSerializer):
    care_items = CareItemSerializer(many=True)
    care_on_demand = CareOnDemandSerializer(many=True)
    medication_items = MedicationItemSerializer(many=True)

    class Meta:
        model = HealthCare
        fields = ('patient', 'doc_reference',
                  'pathology', 'status', 'created_at')
