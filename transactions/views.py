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
from dentists.forms import DentistsForm, DentistsEditForm
from dentists.models import Dentists, Specialization
from dentists.services import create_dentist_data
from transactions.models import Transactions
from transactions.forms import TrxForm


class TrxIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'transactions/index.html'
    page_title = 'Transactions Dashboard'
    order_by_default = ['-trx_date', '-trx_number']
#     search_form = ProductSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(TrxIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return Transactions.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(TrxIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class TrxNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Transactions
    template_name = 'transactions/new.html'
    form_class = TrxForm

    def dispatch(self, request, *args, **kwargs):
        return super(TrxNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('dentists_index')

    def get_context_data(self, **kwargs):
        context = super(TrxNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = DentistsForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('dentists/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        #         create_dentist_data(form.cleaned_data)
        return super(TrxNewView, self).form_valid(form)
