from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView

# local
from mainapp.forms import PackageForm
from mainapp.models import Package


class PackageList(ListView):
    model = Package
    context_object_name = "package_list"
    template_name = 'main/package/list.html'

    def get_queryset(self):
        query = self.request.GET.get("s")
        if query:
            return Package.objects.filter(name__startswith=query)
        else:
            return Package.objects.order_by("-id")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Authors'
        data['form'] = PackageForm()
        return data


def add_package(request):
    package_form = PackageForm()

    if request.method == "POST":
        package_form = PackageForm(request.POST)
        if package_form.is_valid():
            package_form.save()

    context = {
        'form': package_form
    }
    return render(request, 'main/package/add.html', context)


def edit_package(request, id):
    package = Package.objects.get(pk=id)
    package_form = PackageForm(instance=package)

    if request.method == "POST":
        package_form = PackageForm(instance=package, data=request.POST)
        package_form.save()
    context = {
        'form': package_form
    }
    return render(request, 'main/package/add.html', context)


def delete_package(request, id):
    if request.method == "POST":
        package = Package.objects.get(pk=id)
        package.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
