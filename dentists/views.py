from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db import transaction
from django.db.models.aggregates import Count
from django.forms.fields import DateField
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
from dentists.forms import DentistsNewForm, DentistsEditForm
from dentists.models import Dentists, Specialization


class DentistsIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'dentists/index.html'
    page_title = 'Dentists Dashboard'
    order_by_default = ['-created_time', '-id']
#     search_form = ProductSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(DentistsIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return Dentists.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(DentistsIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class DentistsNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Dentists
    template_name = 'dentists/new.html'
    form_class = DentistsNewForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('dentists_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(DentistsNewView, self).form_invalid(form)


class DentistsEditView(UpdateView):
    form_class = DentistsEditForm
    template_name = 'dentists/edit.html'
    model = Dentists

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("dentists_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(DentistsEditView, self).form_invalid(form)
