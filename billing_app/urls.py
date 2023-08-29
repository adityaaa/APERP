from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('purchase/', views.purchase_list, name='purchase_list'),
    path('finance/', views.invoice_list, name='invoice_list'),
    path('hr/', views.department_list, name='department_list'),
    # path('sales/', views.sales_list, name='sales_list'),
    
]