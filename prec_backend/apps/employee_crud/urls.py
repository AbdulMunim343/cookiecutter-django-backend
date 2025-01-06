from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteAPIView.as_view(), name='employee-detail'),
]
