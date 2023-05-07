from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import TransactionDebitForm,TransactionCreditForm
from django.contrib import messages
from .models import Transaction
from django.db.models import Sum
# Create your views here.


#Expense list view
def expense_list(request):
    expense = Transaction.objects.filter(cr=0)
    paginator = Paginator(expense, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #Logic to add expense
    expense_form = TransactionDebitForm
    if request.method == "POST":
        expense_form = expense_form(data=request.POST)
        expense_form.save()
        messages.success(request,'Expense has been added!')
        return redirect(reverse('expense_list'))
    context = {
        'page_obj': page_obj,
        'form':expense_form,
    }
    return render(request, 'expense_list.html', context)

#Income list view
def income_list(request):
    expense = Transaction.objects.filter(dr=0)
    paginator = Paginator(expense, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #logic to add income
    income_form = TransactionCreditForm
    if request.method == "POST":
        income_form = income_form(data=request.POST)
        income_form.save()
        messages.success(request,'Income has been added!')
        return redirect(reverse('income_list'))

    context = {
        'page_obj': page_obj,
        'form':income_form,
    }
    return render(request, 'income_list.html', context)

#Add Expense
def add_expense(request):
    expense_form = TransactionDebitForm
    if request.method == "POST":
        expense_form = expense_form(data=request.POST)
        expense_form.save()
        messages.success(request,'Expense has been added!')
        return redirect(reverse('expense_list'))
    context={
        'form':expense_form,
    }
    return render(request,'add_expense.html',context)


#Add Income
def add_income(request):
    expense_form = TransactionDebitForm
    if request.method == "POST":
        expense_form = expense_form(data=request.POST)
        expense_form.save()
        messages.success(request,'Expense has been added!')
        return redirect(reverse('expense_list'))
    context={
        'form':expense_form,
    }
    return render(request,'add_expense.html',context)

#Edit existing transaction
def edit_transaction(request, id):
    expense = Transaction.objects.get(pk=id)
    if(expense.cr==0):
        expense_form = TransactionDebitForm(instance=expense)
        txt="Edit Expense"
    else:
        expense_form = TransactionCreditForm(instance=expense)
        txt="Edit Income"
    if request.method == "POST":
        if (expense.cr == 0):
            expense_form = TransactionDebitForm(instance=expense, data=request.POST)
        else:
            expense_form = TransactionCreditForm(instance=expense, data=request.POST)
        expense_form.save()
        messages.info(request,'Transaction has been edited.')
        return redirect(reverse('income_list'))
    context = {
        'form': expense_form,
        'txt':txt
    }
    return render(request, 'add_expense.html', context)

#Delete transaction
def delete_transaction(request, id):
    if request.method == "POST":
        exp_obj = Transaction.objects.get(pk=id)
        exp_obj.delete()
        messages.warning(request,'Transaction has been deleted.')
    return redirect(reverse('expense_list'))

#Showing Expense by Category
def transaction_report(request):
    total_income = Transaction.objects.filter(cr__gt=0).aggregate(Sum('cr'))['cr__sum'] or 0
    total_expense = Transaction.objects.filter(dr__gt=0).aggregate(Sum('dr'))['dr__sum'] or 0
    total_profit = round(total_income - total_expense, 2)
    income_by_category = Transaction.objects.filter(cr__gt=0).values('cat__name').annotate(Sum('cr'))
    expense_by_category = Transaction.objects.filter(dr__gt=0).values('cat__name').annotate(Sum('dr'))

    context={
        'total_income': total_income,
        'total_expense': total_expense,
        'total_profit': total_profit,
        'income_by_category': income_by_category,
        'expense_by_category': expense_by_category,
    }
    return render(request,'transaction_report.html',context)
