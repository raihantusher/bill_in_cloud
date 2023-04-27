from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView

# local
from mainapp.forms import CustomerForm
from mainapp.models import CustomerProfile


class CustomerList(ListView):
    model = CustomerProfile
    context_object_name = "customer_list"
    template_name = 'main/customer/list.html'

    def get_queryset(self):
        query = self.request.GET.get("s")
        if query:
            return CustomerProfile.objects.filter(name__startswith=query)
        else:
            return CustomerProfile.objects.order_by("-id")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Authors'
        return data


def add_customer_profile(request):
    customer_form = CustomerForm()

    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()

    context = {
        'customer_form': customer_form
    }
    return render(request, 'main/customer/add.html', context)


def edit_customer_profile(request, id):
    customer = CustomerProfile.objects.get(pk=id)
    customer_form = CustomerForm(instance=customer)

    if request.method == "POST":
        customer_form = CustomerForm(instance=customer, data=request.POST)
        customer_form.save()
    context = {
        'customer_form': customer_form
    }
    return render(request, 'main/customer/add.html', context)


def delete_customer(request, id):
    if request.method == "POST":
        customer = CustomerProfile.objects.get(pk=id)
        customer.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
