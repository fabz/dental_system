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
            return render_to_response('dentists/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        #         create_dentist_data(form.cleaned_data)
        return super(NewView, self).form_valid(form)


class EditView(FormView):
    form_class = DentistsEditForm
    template_name = 'dentists/edit.html'
    model = Dentists

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        return super(EditView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = Dentists.objects.get(id=self.pk)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        try:
            dentist = Dentists.objects.get(id=self.pk)
            form = DentistsEditForm(data=self.request.POST, dentist=dentist)
        except Dentists.DoesNotExist:
            messages.error(request, _('Dentist data does not exist'))
            return HttpResponseRedirect(urlresolvers.reverse('dentists_index'))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class):
        dentist = Dentists.objects.get(id=self.pk)
        return form_class(dentist=dentist)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('dentists_index')

    def form_invalid(self, form, message='Changes fail to save'):
        messages.add_message(self.request, messages.ERROR, message)
        self.object = Dentists.objects.get(id=self.pk)
        return super(EditView, self).form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        try:
            dentist_obj = Dentists.objects.select_for_update().get(id=self.pk)
            set_attributes(form.cleaned_data, dentist_obj)
            dentist_obj.save()
        except Dentists.DoesNotExist:
            self.form_invalid(form, "Dentist not found")
