import json
from os.path import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.contrib import messages
from django.db import IntegrityError
from django.db import transaction
from django.db.models.aggregates import Count
from django.utils import timezone
from django.views.generic.edit import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from dentists.forms import DentistsForm
from dentists.models import Dentists, Specialization


class IndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'dentists/index.html'
    page_title = 'Dentists Dashboard'
    order_by_default = ['-created_time', '-id']
#     search_form = ProductSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return Dentists.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        url_params = self.request.GET
        categories = filter(None, url_params.getlist('categories'))

        return context_data


class NewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Dentists
    template_name = 'dentists/new.html'
    form_class = DentistsForm

    def dispatch(self, request, *args, **kwargs):
        return super(NewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('dentists_index')

    def get_context_data(self, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(NewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = DentistsForm(self.request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        clean_form = form.cleaned_data
        print(clean_form)
        x = Dentists.objects.create(name=clean_form['name'], email=clean_form['email'] + 'z', address=clean_form['address'],
                                    phone_number=clean_form['phone_number'] + '1', specialization=clean_form['specialization'])
        return super(NewView, self).form_valid(form)
