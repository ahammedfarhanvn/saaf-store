from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home, add_customer, add_customers, customer_list, add_money, item_purchase, get_customer_details, add_item, item_list, edit_item, delete_item, export_customers, edit_customer, delete_customer, check_wallet_balance

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html',redirect_authenticated_user=True), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('add_customer/', add_customer, name='add_customer'),
    path('add_customers/', add_customers, name='add_customers'),
    path('customers/', customer_list, name='customer_list'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    
    path('item_purchase/', item_purchase, name='item_purchase'),
    path('transactions/', views.all_transactions, name='transactions'),

    path('add_item/', add_item, name='add_item'),
    path('item_list/', item_list, name='item_list'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),  
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    
    path('add_money/<int:customer_id>/', add_money, name='add_money'),
    
    path('export/customers/', views.export_customers_excel, name='export_customers_excel'),
    path('export_customers/', export_customers, name='export_customers'),
    path('check_wallet_balance/', check_wallet_balance, name='check_wallet_balance'),
    path('check_wallet_balance/', views.check_wallet_balance, name='check_wallet_balance'),
    path('get_customer_details/<str:customer_number>/', get_customer_details, name='get_customer_details'),
    
]
