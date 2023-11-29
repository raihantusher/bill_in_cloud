from django.urls import path
from .views import AllReportsView, IncomeStatement

urlpatterns = [
    path("reports/", AllReportsView.as_view(), name="reports"),
    path("reports/income_statement/", IncomeStatement.as_view(), name="income_statement"),
]