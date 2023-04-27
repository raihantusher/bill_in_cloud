from django.urls import path
from .views import package_views, profile_views


urlpatterns = [
    path('customer/add', profile_views.add_customer_profile, name="add_new_customer"),
    path('customer/list/', profile_views.CustomerList.as_view(), name="list_customer"),
    path('customer/<int:id>/edit', profile_views.edit_customer_profile, name="edit_customer"),
    path('customer/<int:id>/delete', profile_views.delete_customer, name="delete_customer"),

    path('package/add', package_views.add_package, name="add_new_package"),
    path('package/list/', package_views.PackageList.as_view(), name="list_package"),
    path('package/<int:id>/edit', package_views.edit_package, name="edit_package"),
    path('package/<int:id>/delete', package_views.delete_package, name="delete_package"),

]
