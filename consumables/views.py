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
from consumables.forms import *
from consumables.models import *


class ConsumablesIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'consumables/index.html'
    page_title = 'consumables Dashboard'
    order_by_default = ['-created_time', '-id']
    search_form = ConsumableSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(ConsumablesIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        if self.request.GET.get('sku', None) or self.request.GET.get('name', None) or self.request.GET.get('is_sellable', None):
            return ConsumablesPricing.objects.select_related('consumable').filter(sku__icontains=self.request.GET['sku'], name__icontains=self.request.GET['name'], is_sellable=self.request.GET['is_sellable'])
            #return Consumables.objects.filter(sku__icontains=self.request.GET['sku'], name__icontains=self.request.GET['name'], is_sellable=self.request.GET['is_sellable'])
        else:
            return ConsumablesPricing.objects.all().select_related('consumable')

    def get_context_data(self, **kwargs):
        context_data = super(ConsumablesIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class ConsumablesNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Consumables
    template_name = 'consumables/new.html'
    form_class = ConsumablesForm
    
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('consumables_index',kwargs={'consumable_id': self.kwargs['consumable_id']})

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(ConsumablesNewView, self).form_invalid(form)
    
#    def form_valid(self,form):
#        consumablespricing = form.save(commit=False)
#        consumablespricing.consumable = self.request.consumables
#        
#        ConsumablesPricing(sell_price = )
#       return super(ConsumablesNewView, self).form_valid(form)

def form_valid(self, form):
    
        article = form.save(commit=False)
        article.author = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(CreateArticle, self).form_valid(form)


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
