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
from treatments.models import Treatments
from treatments.forms import TreatmentsEditForm, TreatmentsNewForm


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
    template_name = 'dentists/new.html'
    form_class = TreatmentsNewForm

    def dispatch(self, request, *args, **kwargs):
        return super(TreatmentsNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('treatments_index')

    def get_context_data(self, **kwargs):
        context = super(TreatmentsNewView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TreatmentsNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = TreatmentsNewForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('treatments/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        return super(TreatmentsNewView, self).form_valid(form)


class TreatmentsEditView(FormView):
    form_class = TreatmentsEditForm
    template_name = 'dentists/edit.html'
    model = Treatments

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        return super(TreatmentsEditView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = Treatments.objects.get(id=self.pk)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        try:
            dentist = Treatments.objects.get(id=self.pk)
            form = TreatmentsEditView(data=self.request.POST, dentist=dentist)
        except Treatments.DoesNotExist:
            messages.error(request, _('Dentist data does not exist'))
            return HttpResponseRedirect(urlresolvers.reverse('dentists_index'))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class):
        dentist = Treatments.objects.get(id=self.pk)
        return form_class(dentist=dentist)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('dentists_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Treatments.objects.get(id=self.pk)
        return super(TreatmentsEditView, self).form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        try:
            treatment_obj = Treatments.objects.select_for_update().get(id=self.pk)
            set_attributes(form.cleaned_data, treatment_obj)
            treatment_obj.save()
        except Treatments.DoesNotExist:
            self.form_invalid(form, "Dentist not found")
