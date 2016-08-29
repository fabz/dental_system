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
from transactions.forms import TrxNewForm
from transactions.models import Transactions, TransactionDetail


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
    form_class = TrxNewForm

    def dispatch(self, request, *args, **kwargs):
        return super(TrxNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('trxs_index')

    def get_context_data(self, **kwargs):
        context = super(TrxNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = TrxNewForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('transactions/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TrxNewView, self).form_valid(form)


class TrxDetailIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'transactions/detail_index.html'
    page_title = 'Transaction Details Dashboard'
    order_by_default = ['-trx_date', '-trx_number']
#     search_form = ProductSearchForm

    transaction_id = ''

    def dispatch(self, request, *args, **kwargs):
        global transaction_id
        transaction_id = args[0]
        return super(TrxDetailIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        print("transaction_id", transaction_id)
        transaction_obj = Transactions.objects.get(trx_number=transaction_id)
        return TransactionDetail.objects.filter(transaction=transaction_obj)

    def get_context_data(self, **kwargs):
        context_data = super(TrxDetailIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class TrxDetailNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Transactions
    template_name = 'transactions/detail_new.html'
    form_class = TrxNewForm

    def dispatch(self, request, *args, **kwargs):
        return super(TrxNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('trxs_index')

    def get_context_data(self, **kwargs):
        context = super(TrxNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = TrxNewForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('transactions/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TrxNewView, self).form_valid(form)