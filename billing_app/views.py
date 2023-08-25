from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def inventory_list(request):
    # Add logic to fetch and display inventory data
    return render(request, 'inventory_list.html')

def purchase_list(request):
    # Add logic to fetch and display purchase data
    return render(request, 'purchase_list.html')

def invoice_list(request):
    # Add logic to fetch and display invoice data
    return render(request, 'invoice_list.html')

def department_list(request):
    # Add logic to fetch and display department data
    return render(request, 'department_list.html')
