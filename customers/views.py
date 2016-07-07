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
#     search_form = ProductSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(CustomersIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
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

    def dispatch(self, request, *args, **kwargs):
        return super(CustomersNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('customers_index')

    def get_context_data(self, **kwargs):
        context = super(CustomersNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(CustomersNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = CustomersForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('customers/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        return super(CustomersNewView, self).form_valid(form)


class CustomersEditView(FormView):
    form_class = CustomersEditForm
    template_name = 'customers/edit.html'
    model = Customer

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        return super(CustomersEditView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = Customer.objects.get(id=self.pk)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=self.pk)
            form = CustomersEditForm(data=self.request.POST, customer=customer)
        except Customer.DoesNotExist:
            messages.error(request, _('Customer data does not exist'))
            return HttpResponseRedirect(urlresolvers.reverse('customers_index'))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class):
        customer = Customer.objects.get(id=self.pk)
        return form_class(customer=customer)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('customers_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Customer.objects.get(id=self.pk)
        return super(CustomersEditView, self).form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        try:
            customer_obj = Customer.objects.select_for_update().get(id=self.pk)
            set_attributes(form.cleaned_data, customer_obj)
            customer_obj.save()
        except Customer.DoesNotExist:
            self.form_invalid(form, "Customer not found")
