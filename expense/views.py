from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import ExpensesList
from django.http import HttpResponseRedirect
from .forms import TransactionDebitForm
from django.contrib import messages
# Create your views here.


#Expense list views
def expense_list(request):
    expense = ExpensesList.objects.all()
    paginator = Paginator(expense, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj
    }
    return render(request, 'expense_list.html', context)

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
#Edit existing expenses
def edit_expense(request, id):
    expense = ExpensesList.objects.get(pk=id)
    expense_form = ExpenseForm(instance=expense)

    if request.method == "POST":
        expense_form = ExpenseForm(instance=expense, data=request.POST)
        expense_form.save()
        messages.info(request,'Expense has been edited.')
        return redirect(reverse('expense_list'))
    context = {
        'form': expense_form,
        'txt':'Edit Expense'
    }
    return render(request, 'add_expense.html', context)

#Delete expense
def delete_expense(request, id):
    if request.method == "POST":
        exp_obj = ExpensesList.objects.get(pk=id)
        exp_obj.delete()
        messages.warning(request,'Expense item has been deleted.')
    return redirect(reverse('expense_list'))
