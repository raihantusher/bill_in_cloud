from django.urls import path
from .views import AllReportsView, IncomeStatement

urlpatterns = [
    path("report/", AllReportsView.as_view(), name="report"),
    path("report/income_statement/", IncomeStatement.as_view(), name="income_statement"),
]