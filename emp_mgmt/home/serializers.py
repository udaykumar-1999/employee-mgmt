from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    def validate_age(self, value):
        if value > 60 :
            raise serializers.ValidationError("age cannot be greater than 60")
        return value
    
    def validate_gender(self, value):
        if value not in ['M', 'F', 'T']:
            raise serializers.ValidationError("gender cannot be other than (M)-Male, (F)-Female, (T)-Transgender")
        return value 

