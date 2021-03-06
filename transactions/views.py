import traceback

from django.contrib import messages
from django.core import urlresolvers
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.edit import CreateView, FormView, UpdateView

from dental_system.views import DentalSystemListView, add_pagination, add_success_message, prepare_form_with_file_if_exist, add_error_message
from transactions.forms import TrxNewForm, TrxEditForm, TrxDetailNewForm, TrxDetailEditForm
from transactions.models import Transactions, TransactionDetail
from treatments.models import Treatments


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
        return Transactions.objects.all().order_by('-created_time')

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
        print("customer", form.fields['customer'])
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('transactions/new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TrxNewView, self).form_valid(form)


class TrxEditView(UpdateView):
    form_class = TrxEditForm
    template_name = 'transactions/edit.html'
    model = Transactions

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse("trxs_index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxEditView, self).form_invalid(form)


class TrxDetailIndexView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'transactions/detail_index.html'
    page_title = 'Transaction Details Dashboard'
    order_by_default = ['-trx_date', '-trx_number']
    transaction_id = ''

    def dispatch(self, request, *args, **kwargs):
        global transaction_id
        transaction_id = args[0]
        return super(TrxDetailIndexView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        transaction_obj = Transactions.objects.get(id=transaction_id)
        trx_details = TransactionDetail.objects.filter(transaction=transaction_obj)
        for trx in trx_details:
            trx.detail_type = eval(trx.detail_type).objects.get(id=trx.detail_id).name
        return trx_details

    def get_context_data(self, **kwargs):
        context_data = super(TrxDetailIndexView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)
        context_data['transaction_id'] = transaction_id
        print('context_data', context_data)

        return context_data


class TrxDetailNewView(CreateView):
    """
    handle product category list
    /products/
    """

    model = TransactionDetail
    template_name = 'transactions/detail_new.html'
    form_class = TrxDetailNewForm
    transaction_id = ''

    def dispatch(self, request, *args, **kwargs):
        global transaction_id
        transaction_id = args[0]
        return super(TrxDetailNewView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return form_class(transaction_id=transaction_id)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Changes successfully saved')
        return urlresolvers.reverse('trxs_detail_index', args=(transaction_id,))

    def get_context_data(self, **kwargs):
        context = super(TrxDetailNewView, self).get_context_data(**kwargs)
        context['transaction_id'] = transaction_id
        context['back_url'] = urlresolvers.reverse('trxs_detail_index', args=(transaction_id,))
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxDetailNewView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = TrxDetailNewForm(self.request.POST, transaction_id=transaction_id)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return render_to_response('transactions/detail_new.html', {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TrxDetailNewView, self).form_valid(form)


class TrxDetailEditView(UpdateView):
    form_class = TrxDetailEditForm
    template_name = 'transactions/detail_edit.html'
    model = TransactionDetail
    transaction_id = ''

    def dispatch(self, request, *args, **kwargs):
        global transaction_id
        transaction_id = TransactionDetail.objects.get(id=kwargs.pop('pk')).transaction.id
        return super(TrxDetailEditView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        add_success_message(self.request)
        return urlresolvers.reverse('trxs_detail_index', args=(transaction_id,))

    def get_context_data(self, **kwargs):
        context = super(TrxDetailEditView, self).get_context_data(**kwargs)
        context['transaction_id'] = transaction_id
        context['back_url'] = urlresolvers.reverse('trxs_detail_index', args=(transaction_id,))
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Changes fail to save')
        return super(TrxEditView, self).form_invalid(form)


class TrxDetailPrintView(DentalSystemListView):
    """
    handle product category list
    /products/
    """
    template_name = 'transactions/detail_views.html'
    page_title = 'Transaction Details Dashboard'
    order_by_default = ['-trx_date', '-trx_number']
    transaction_id = ''

    def dispatch(self, request, *args, **kwargs):
        global transaction_id
        transaction_id = args[0]
        return super(TrxDetailPrintView, self).dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        transaction_obj = Transactions.objects.get(id=transaction_id)
        trx_details = TransactionDetail.objects.filter(transaction=transaction_obj)
        for trx in trx_details:
            treatment_obj = eval(trx.detail_type).objects.get(id=trx.detail_id)
            trx.detail_type = treatment_obj.name
            trx.treatment_price = treatment_obj.prices.price
            if trx.discount > 0:
                trx.remarks = 'Discount: -{}'.format(str(int(trx.discount)))
            else:
                trx.remarks = '-'
        return trx_details

    def get_context_data(self, **kwargs):
        context_data = super(TrxDetailPrintView, self).get_context_data(**kwargs)
        context_data = add_pagination(self.request, context_data)
        trx_obj = Transactions.objects.get(id=transaction_id)
        trx_detail_obj = trx_obj.transactiondetail_set.all()
        context_data['transaction_id'] = transaction_id
        context_data['trx_amount'] = int(sum(list(trx_detail_obj.values_list('price', flat=True))))
        context_data['customer_name'] = trx_obj.customer.name
        context_data['dentists_name'] = trx_obj.dentist.name
        context_data['trx_data'] = trx_obj

        return context_data
