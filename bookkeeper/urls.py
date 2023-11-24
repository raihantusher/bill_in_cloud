from django.urls import path
from .views import AllReportsView, IncomeStatement

urlpatterns = [
    path("report/", AllReportsView.as_view()),
    path("report/income_statement/", IncomeStatement.as_view()),
]