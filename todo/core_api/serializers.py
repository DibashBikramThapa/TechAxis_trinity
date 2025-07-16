from rest_framework import serializers

from auth_api.serializers import UserMinimalSerializer
from core.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        fields['created_by'] = serializers.SerializerMethodField()
        return fields

    def get_created_by(self, obj):
        return UserMinimalSerializer(obj.created_by).data



class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'description', 'deadline')

        extra_kwargs = {
            'deadline': {'required': True}
        }

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
