from home.views import EmployeeViews
from django.urls import path

urlpatterns = [
    path('employees/', EmployeeViews.as_view()),
    path('employees/<int:id>', EmployeeViews.as_view())
]
