from django.urls import path
from .views import *
urlpatterns = [
    path('expense_list/',expense_list,name='expense_list'),
    path('income_list/',income_list,name='income_list'),
    path('expense/add/',add_expense,name='add_expense'),
    path('income/add/',add_income,name='add_income'),
    path('edit/<int:id>/',edit_transaction, name="edit_expense"),
    path('delete/<int:id>/',delete_transaction, name="delete_expense"),
    path('expense_list/category',transaction_report,name="expense_by_category")

]