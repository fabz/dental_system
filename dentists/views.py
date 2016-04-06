import json
from os.path import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db import IntegrityError
from django.db import transaction
from django.db.models.aggregates import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from dentists.models import Dentists


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
        return Dentists.active.all()

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        url_params = self.request.GET
        categories = filter(None, url_params.getlist('categories'))

        return context_data


class NewView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
#     template_name = 'dentists/new.html'
# #     form_class = ProductNewForm
#
#     def get_success_url(self):
#         add_success_message(self.request)
#         return urlresolvers.reverse('product_index')
#
#     def form_valid(self, form):
#         form = prepare_form_with_file_if_exist(form, 'image')
#         return save_form_data(settings.PRODUCT_API_PATH, form, self, 'product_index')
#
#     def form_invalid(self, form):
#         add_error_message(self.request)
#         return super(NewView, self).form_invalid(form)
    pass
