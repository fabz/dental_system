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
from itertools import chain

from consumables.forms import *
from consumables.models import *
from consumables.services import *
from dental_system.helpers import set_attributes
from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message


class ConsumablesIndexView(DentalSystemListView):
    """
    DONE
    """
    template_name = 'consumables/index.html'
    page_title = 'consumables Dashboard'
    order_by_default = ['-created_time', '-id']
    search_form = ConsumableSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(ConsumablesIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        if self.request.GET.get('is_sellable', None):
            return Consumables.objects.filter(sku__icontains=self.request.GET['sku'], name__icontains=self.request.GET['name'], is_sellable=self.request.GET['is_sellable'])
        elif self.request.GET.get('sku', None) or self.request.GET.get('name', None):
            return Consumables.objects.filter(sku__icontains=self.request.GET['sku'], name__icontains=self.request.GET['name'])
        else:
            return Consumables.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(ConsumablesIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class ConsumablesNewView(FormView):
    """
    DONE
    """

    model = Consumables
    template_name = 'consumables/new.html'
    form_class = ConsumablesForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('consumables_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesNewView, self).form_invalid(form)

    def form_valid(self, form):
        create_new_consumables(form.cleaned_data)
        return super(ConsumablesNewView, self).form_valid(form)


class ConsumablesEditView(FormView):

    '''
    Done
    '''

    form_class = ConsumablesEditForm
    template_name = 'consumables/edit.html'
    model = Consumables

    def get_success_url(self):
        add_success_message(self.request)
        return HttpResponseRedirect(urlresolvers.reverse("consumables_index"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesEditView, self).form_invalid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class(consumable=kwargs['pk'])
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        cons_price_id = kwargs['pk']
        sell_price = float(request.POST['sell_price'])
        sku = request.POST['sku']

        with transaction.atomic():
            consumablespricing_obj = ConsumablesPricing.objects.get(consumable=cons_price_id, end_date=None)
            if consumablespricing_obj.sell_price != sell_price:
                create_new_pricing(consumablespricing_obj, sell_price, sku)
        return self.get_success_url()


class ConsumablesMutationNewView(UpdateView):
    """
    handle product category list
    /products/
    """

    model = Consumables
    template_name = 'consumables/mutation_new.html'
    form_class = ConsumablesMutationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return HttpResponseRedirect(urlresolvers.reverse('consumables_index'))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesMutationNewView, self).form_invalid(form)

    def form_valid(self, form):
        create_new_consumables_mutation(form.cleaned_data)
        return self.get_success_url()


class ConsumablesMutationHistView(DentalSystemListView):
    template_name = 'consumables/mutation_hist.html'
    page_title = 'Mutation History'
    order_by_default = ['-created_time', '-id']
    #search_form = ConsumableSearchForm

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super(ConsumablesMutationHistView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return ConsumablesStockMutation.objects.filter(consumable=self.pk)

    def get_context_data(self, **kwargs):
        context_data = super(ConsumablesMutationHistView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)
        return context_data
