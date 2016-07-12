from django.contrib import messages
from django.core import urlresolvers
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, FormView

from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from prices.models import Prices
from prices.services import create_price_history
from treatments.forms import TreatmentsEditPriceForm
from treatments.models import Treatments


FIELDS = ['name', 'description', 'treatment_type']


class TreatmentsIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'treatments/index.html'
    page_title = 'Treatments Dashboard'
    order_by_default = ['-created_time', '-id']
#     search_form = ProductSearchForm

    def dispatch(self, request, *args, **kwargs):
        return super(TreatmentsIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return Treatments.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(TreatmentsIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)

        return context_data


class TreatmentsNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = Treatments
    template_name = 'treatments/new.html'
    fields = FIELDS

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('treatments_index')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TreatmentsNewView, self).form_invalid(form)


class TreatmentsEditView(UpdateView):
    fields = FIELDS
    template_name = 'treatments/edit.html'
    model = Treatments

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('treatments_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Treatments.objects.get(id=self.pk)
        return super(TreatmentsEditView, self).form_invalid(form)


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
