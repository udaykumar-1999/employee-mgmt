from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404


class EmployeeViews(APIView):
    
    # list of all employees or employee with id
    def get(self, request, id=None):
        if id:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        items = Employee.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
    # create new employees
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # update an existing employee  
    def patch(self, request, id=None):
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"data": serializer.errors})

    # delete an employee  
    def delete(self, request, id=None):
        if id:
            emp = get_object_or_404(Employee, id=id)
            emp.delete()
            return Response({"data": "Employee Deleted"})
        return Response({"data": "Employee Not Found"})

