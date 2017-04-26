from rest_framework import serializers
from workers.models import Employee, JobPosition


class JobPositionSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()

    # created = serializers.DateTimeField()

    class Meta:
        model = JobPosition
        fields = ('id', 'name')


class JobPositionPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return 'JobPosition: %s' % (instance.name)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_working', 'position')

    # def create(self, validated_data):
    #     emp_data = validated_data.pop('position')
    #     employee = Employee.objects.create(**validated_data)
    #     JobPosition.objects.create(employee=employee, **emp_data)
    #     return employee
