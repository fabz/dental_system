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
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('vendors_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(VendorsNewView, self).form_invalid(form)


class VendorsEditView(UpdateView):
    form_class = VendorsEditForm
    template_name = 'vendors/edit.html'
    model = Vendors

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("vendors_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(VendorsEditView, self).form_invalid(form)
