from django.contrib import messages
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db.models.aggregates import Count
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import timezone
from django.views.generic.edit import CreateView, FormView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()

        data = Dentists.objects.get(id=kwargs.get('id')).__dict__

        form = self.get_forms(form_class, data)
        return self.render_to_response(self.get_context_data(form=form))
#
#     def dispatch(self, request, *args, **kwargs):
#         self.pk = kwargs.get('id')
#         return super(FormView, self).dispatch(request, *args, **kwargs)

#     def get_form_class(self):
#         return FormView.get_form_class(self)

#     def get_form(self, form_class):
#         dentist = Dentists.objects.get(id=self.pk)
#         return form_class(dentist, **self.get_form_kwargs())

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        form = DentistsEditForm(self.request.POST, instance=Dentists.objects.get(id=kwargs.get('id')))
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_forms(self, form_class, data=None):
        if self.request.method == "GET":
            return form_class(data, **self.get_form_kwargs())
        else:
            return form_class(**self.get_form_kwargs())

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('dentists_index')

#     def form_valid(self, form):
#         form = prepare_form_with_file_if_exist(form, 'image')
#         success_flag = post_form_to_backend(self.request, form)
#         return form_valid_redirection_after_edit(self, form, success_flag, 'product_index', None, True)
#
#     def form_invalid(self, form):
#         add_error_message(self.request)
#         return super(EditView, self).form_invalid(form)
