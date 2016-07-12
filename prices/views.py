from django.contrib import messages
from django.core import urlresolvers
from django.db import transaction
from django.views.generic.edit import CreateView, UpdateView

from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from prices.forms import PricesEditForm
from prices.models import Prices, PricesHistories
from treatments.models import Treatments


FIELDS = ['treatments', 'price']


class PricesEditView(CreateView):
    #     fields = FIELDS
    form_class = PricesEditForm
    template_name = 'treatments/edit_prices.html'
    model = Prices

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk', None)
        return super(PricesEditView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('treatments_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Treatments.objects.get(id=self.pk)
        return super(PricesEditView, self).form_invalid(form)

    def form_valid(self, form):
        print('udah masuk sini', form.cleaned_data)
        try:
            price_obj = Prices.objects.get(treatments=form.cleaned_data['treatments'])
            price_obj.price = form.cleaned_data['price']
            price_obj.save()
        except Prices.DoesNotExist:
            Prices.objects.create(treatments=form.cleaned_data['treatments'], price=form.cleaned_data['price'])
        return self.get_success_url(self)
