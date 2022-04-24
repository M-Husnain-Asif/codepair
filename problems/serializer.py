from rest_framework.serializers import ModelSerializer
from .models import Problems

class ProblemsSerializer(ModelSerializer):
    class Meta:
        model = Problems
        fields ='__all__'