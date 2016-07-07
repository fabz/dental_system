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
from vendors.forms import *
from vendors.models import *


class VendorsIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'vendors/index.html'
    page_title = 'Vendors Dashboard'
    order_by_default = ['-created_time', '-id']
    search_form = VendorSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(VendorsIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        if self.request.GET.get('name', None):
            return Vendors.objects.filter(name__icontains=self.request.GET['name'])
        else:
            return Vendors.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(VendorsIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class VendorsNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Vendors
    template_name = 'vendors/new.html'
    form_class = VendorsForm

    def dispatch(self, request, *args, **kwargs):
        return super(VendorsNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('vendors_index')

    def get_context_data(self, **kwargs):
        context = super(VendorsNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(VendorsNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = VendorsForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('vendors/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        return super(VendorsNewView, self).form_valid(form)


class VendorsEditView(FormView):
    form_class = VendorsEditForm
    template_name = 'vendors/edit.html'
    model = Vendors

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        return super(VendorsEditView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = Vendors.objects.get(id=self.pk)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        try:
            vendor = Vendors.objects.get(id=self.pk)
            form = VendorsEditForm(data=self.request.POST, vendor=vendor)
        except Vendors.DoesNotExist:
            messages.error(request, _('Vendor data does not exist'))
            return HttpResponseRedirect(urlresolvers.reverse('vendors_index'))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class):
        customer = Customer.objects.get(id=self.pk)
        return form_class(customer=customer)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('vendors_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Vendors.objects.get(id=self.pk)
        return super(VendorsEditView, self).form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        try:
            vendor_obj = Vendors.objects.select_for_update().get(id=self.pk)
            set_attributes(form.cleaned_data, vendor_obj)
            vendor_obj.save()
        except Vendors.DoesNotExist:
            self.form_invalid(form, "Vendor not found")
