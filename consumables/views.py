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
    TO DO:
    - get price data out in the table
    """
    template_name = 'consumables/index.html'
    page_title = 'consumables Dashboard'
    order_by_default = ['-created_time', '-id']
    search_form = ConsumableSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(ConsumablesIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        if self.request.GET.get('is_sellable', None):
            cons_price = ConsumablesPricing.objects.filter(consumable__sku__icontains=self.request.GET['sku'], consumable__name__icontains=self.request.GET[
                                                           'name'], consumable__is_sellable=self.request.GET['is_sellable'], end_date=None)
            return Consumables.objects.filter(consumablespricing=cons_price)
        elif self.request.GET.get('sku', None) or self.request.GET.get('name', None):
            cons_price = ConsumablesPricing.objects.filter(consumable__sku__icontains=self.request.GET['sku'], consumable__name__icontains=self.request.GET['name'], end_date=None)
            return Consumables.objects.filter(consumablespricing=cons_price)
        else:
            cons_price = ConsumablesPricing.objects.filter(end_date=None)
            return Consumables.objects.filter(consumablespricing=cons_price)

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


class ConsumablesEditView(UpdateView):

    form_class = ConsumablesEditForm
    template_name = 'consumables/edit.html'
    model = Consumables

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("consumables_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesEditView, self).form_invalid(form)

    def form_valid(self, form):
        create_new_pricing(form.cleaned_data)
        return super(ConsumablesEditView, self).form_valid(form)

'''    
class TreatmentsEditPriceView(FormView):
    form_class = TreatmentsEditPriceForm
    template_name = 'treatments/edit_prices.html'

    def get_success_url(self):
        add_success_message(self.request)
        return HttpResponseRedirect(urlresolvers.reverse('treatments_index'))

    def get(self, request, *args, **kwargs):
        form = self.form_class(treat_id=kwargs['pk'])
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        treat_id = kwargs['pk']
        sell_price = float(request.POST['sell_price'])
        try:
            with transaction.atomic():
                price_obj = Prices.objects.get(treatments=Treatments.objects.get(id=treat_id))
                if price_obj.price != sell_price:
                    price_obj.price = sell_price
                    price_obj.save()
                    create_price_history(price_obj)
        except Prices.DoesNotExist:
            with transaction.atomic():
                price_obj = Prices.objects.create(treatments=Treatments.objects.get(id=treat_id), price=sell_price)
                create_price_history(price_obj)
        return self.get_success_url()
  '''


class ConsumablesStockinIndexView(DentalSystemListView):

    template_name = 'consumables/stockin_index.html'
    page_title = 'Consumables - Stock In'
    order_by_default = ['-created_time', '-id']
    #search_form = ConsumableSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(ConsumablesStockinIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        # if self.request.GET.get('sku', None) or self.request.GET.get('name', None) or self.request.GET.get('is_sellable', None):
        #    return ConsumablesPricing.objects.filter(consumable__sku__icontains=self.request.GET['sku'], consumable__name__icontains=self.request.GET['name'], consumable__is_sellable=self.request.GET['is_sellable'])
        # else:
        return ConsumablesStockMutation.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(ConsumablesStockinIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class ConsumablesStockinNewView(UpdateView):
    """
    handle product category list
    /products/
    """

    model = Consumables
    template_name = 'consumables/stockin_new.html'
    form_class = ConsumablesStockinForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('consumables_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesStockinNewView, self).form_invalid(form)

    def form_valid(self, form):
        create_new_consumables_stockin(form.cleaned_data)
        return super(ConsumablesStockinNewView, self).form_valid(form)


class ConsumablesStockinEditView(UpdateView):
    form_class = ConsumablesStockinEditForm
    template_name = 'consumables/stockin_edit.html'
    model = Consumables

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("consumables_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesStockinEditView, self).form_invalid(form)


class ConsumablesStockoutNewView(UpdateView):

    model = Consumables
    template_name = 'consumables/stockout_new.html'
    form_class = ConsumablesStockOutForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('consumables_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesStockOutNewView, self).form_invalid(form)

    def form_valid(self, form):
        create_new_consumables_stockout(form.cleaned_data)
        return super(ConsumablesStockOutNewView, self).form_valid(form)
