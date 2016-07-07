from django.contrib import messages
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db import transaction
from django.db.models.aggregates import Count
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import timezone
from django.views.generic.edit import CreateView, FormView, UpdateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dental_system.helpers import set_attributes
from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from customers.forms import *
from customers.models import Customer, CustomerType


class CustomersIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'customers/index.html'
    page_title = 'Customers Dashboard'
    order_by_default = ['-created_time', '-id']
    search_form = CustomerSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(CustomersIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        if self.request.GET.get('name', None):
            return Customer.objects.filter(name__icontains=self.request.GET['name'])
        else:
            return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(CustomersIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class CustomersNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Customer
    template_name = 'customers/new.html'
    form_class = CustomersForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('customers_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(CustomersNewView, self).form_invalid(form)


class CustomersEditView(UpdateView):
    form_class = CustomersEditForm
    template_name = 'customers/edit.html'
    model = Customer

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("customers_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(CustomersEditView, self).form_invalid(form)
