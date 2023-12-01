from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Transaction


class AllReportsView(TemplateView):
    template_name = "transactions/reports/all.html"


class IncomeStatement(View):

    def get(self, request, *args, **kwargs):
        cash = Transaction.objects.filter(category__name="Cash").first()
        cash = cash.balance()
        print(cash)
        sales = Transaction.objects.filter(category__name="Sales").first()
        sales = sales.balance()

        cost_of_good_sold =  Transaction.objects.filter(category__name="Cost of Goods Sold").first()
        cost_of_good_sold = cost_of_good_sold.balance()

        gross_profit = sales - cost_of_good_sold

        context = {
            'sales_income': sales,

            'cost_of_goods_sold': cost_of_good_sold,
            'gross_profit': gross_profit,

        }
        return render(request, 'transactions/reports/income_statement.html', context)
