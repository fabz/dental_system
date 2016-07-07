from base64 import b64encode
import time

from django.contrib import messages
from django.core import urlresolvers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.utils.translation import ugettext
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

# from django.contrib.auth.decorators import login_required, permission_required
# from django.utils.decorators import method_decorator


class DentalSystemListView(ListView):
    '''
    All list views in Dentaville project should derive from this class.
    The purpose is to standardize all list views, and reduce code duplication as possible.
    '''

#     default_style = NumberFormat.FORMAT_GENERAL
#     bold_style = NumberFormat.FORMAT_TEXT
    datetime_style = 'dd/mm/yyyy hh:mm:ss'
    currency_style = '#,##0'

    # default per_page pagination
    paginate_by = 25
    page_title = ''
    model_label = ''
    model_label_plural = ''
    search_form = None
    query_string = None
    capitalize_title = True
    order_by_default = None
    can_export_excel = False
    get_excel_headers = None  # for export excel
    get_excel_row = None  # for export excel
    excel_sheet_name = None
    summary_list = None
    branch_list = []
    agent_list = []
    limit_url_param = False  # for limiting url length when searching, it'll hijack the form in list_template.html file

    def dispatch(self, request, *args, **kwargs):
        return super(DentalSystemListView, self).dispatch(request, *args, **kwargs)

    def can_add_new_object(self):
        return False

    def can_select_multiple(self):
        return False

    def filter_queryset(self, queryset, form):
        return queryset

    def get_form(self):
        if self.search_form == None:
            return None

        if 'has_search' not in self.request.GET:
            form = self.search_form(view_object=self)
            data = QueryDict('').copy()
            data = form.prepare_initial_data(data)
            form.data = data
        else:
            form = self.search_form(self.request.GET, view_object=self)
        return form

    def get_summary_list(self, queryset):
        '''
        Must be overriden, return list of string
        '''
        return []

    def get_initial_queryset(self):
        return []
#         return self.model.objects.none()

    def get_queryset(self):
        # get the initial queryset
        queryset = self.get_initial_queryset()

        # applying the filter from the form
        form = self.get_form()
        if form != None:
            form.full_clean()  # must be valid
            self.query_string = form.get_query_string()

        queryset = self.filter_queryset(queryset, form)

        # update the summary list info
        self.summary_list = self.get_summary_list(queryset)
        return queryset

    def get(self, request, *args, **kwargs):
        if bool(self.request.GET.get('export_excel', '')):
            return self.export_excel(request, *args, **kwargs)
        return super(DentalSystemListView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if int(self.request.POST.get('query_select_all')) == 1:
            queryset = self.get_queryset()
        else:
            # get the agent list from 'agent_selected'
            object_id_list = map(lambda x: int(x), request.POST.getlist('object_selected'))
            queryset = self.model.objects.filter(id__in=object_id_list)
        self.process_post(request, queryset)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    def process_post(self, request, queryset):
        pass

    def get_export_filename(self):
        return 'exported_file.xlsx'

    def get_export_filename_clear(self):
        return self.get_export_filename().replace(' ', '_')

    def export_excel(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        book = self.get_export_book(queryset)
        filename = self.get_export_filename_clear()

        response = HttpResponse(mimetype='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        book.save(response)
        return response

    def get_context_data(self, **kwargs):
        '''
        Overridden in order to handle per_page GET paramater.
        '''
        self.paginate_by = self.request.GET.get('per_page', self.paginate_by)
        context = super(DentalSystemListView, self).get_context_data(**kwargs)
        if self.capitalize_title:
            if hasattr(self.page_title, '__unicode__'):
                self.page_title = self.page_title.__unicode__()
            self.page_title = self.page_title.title()
        if 'paginator' in context and 'page_obj' in context:
            paginator = context['paginator']
            page_obj = context['page_obj']
            context['page_adder'] = paginator.per_page * (page_obj.number - 1)
        else:
            context['page_adder'] = 0
        context['page_title'] = self.page_title
        context['model_label'] = self.model_label
        context['model_label_plural'] = self.model_label_plural
        context['can_select_multiple'] = self.can_select_multiple()
        context['can_add_new_object'] = self.can_add_new_object()
        context['search_form'] = self.get_form()
        context['advanced_search_query'] = self.query_string
        context['api_url'] = self.request.build_absolute_uri('/')[:-1]
        context['can_export_excel'] = self.can_export_excel
        context['summary_list'] = self.summary_list
        context['limit_url_param'] = self.limit_url_param

        return context


class DeleteView(DeleteView):
    """

    Inheritor should override these members:
    model = Shop
    model_name = 'Shop' (Optional. If not specified, it will use model name instead)
    required_permission = 'ordering.delete_member'
    success_url = 'ordering_member_index'
    """
    model_name = None
    required_permission = None
    success_url = None

    template_name = 'layouts/confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        return super(DeleteView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, ugettext('Record successfully deleted'))
        return urlresolvers.reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context_data = super(DeleteView, self).get_context_data(**kwargs)

        if self.model_name:
            context_data['model_name'] = ugettext(self.model_name)
        else:
            context_data['model_name'] = ugettext(self.model.__name__)

        return context_data


def five_seconds_view(request):
    '''
    Just for testing five seconds problem.
    '''
    seconds = int(request.GET.get('sec', 10))
    time.sleep(seconds)
    return HttpResponse("Halo Moefid")


def ping_view(request):
    '''
    Just for testing if web server is alive.
    '''
    return HttpResponse("Hello")


def prepare_form_with_file_if_exist(form, key):
    image_file = None
    if form.cleaned_data[key]:
        image_file = form.cleaned_data[key]
        form.cleaned_data[key] = b64encode(image_file.read())
        form.cleaned_data['{}_filename'.format(key)] = image_file.name

    return form


def add_success_message(request):
    messages.add_message(request, messages.SUCCESS, ugettext('Changes successfully saved'))


def add_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('Changes fail to save'))


def add_error_load_page_message(request):
    messages.add_message(request, messages.ERROR, ugettext('Data cannot be loaded'))


def add_error_object_not_found_message(request):
    messages.add_message(request, messages.ERROR, ugettext('Object not found'))


def add_backend_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('There are errors on Backend Module. Please Contact Your IT Team'))


def add_general_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('System Failure. Please Contact Your IT Team'))


def add_file_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('System cannot read your file. Please check your uploaded file'))


def add_unicode_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('There are unknown characters. Please check your input before submitting'))


def add_input_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('Your input is not valid'))


def add_specific_error_message(request, e):
    error_msg = ugettext("Data already exist") if 'Duplicate entry' in e else ugettext(e)

    messages.add_message(request, messages.ERROR, error_msg)


def add_no_active_category_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('There are no active categories to be ranked or link is not valid'))


def add_no_active_price_category_error_message(request):
    messages.add_message(request, messages.ERROR, ugettext('There are no active price or bonus configurations for this product'))


def add_pagination(request, context_data):
    paginator = context_data['paginator']
    page_obj = context_data['page_obj']
    context_data['page_adder'] = paginator.per_page * (page_obj.number - 1)
    context_data['request'] = request

    return context_data


def check_response_data(self, flag, form_class, data, url_destination):
    if flag == 0:
        return HttpResponseRedirect(reverse(url_destination))
    else:
        form = self.get_form(form_class, data)
        return self.render_to_response(self.get_context_data(form=form))


def get_failed_url(url, url_args):
    if url_args:
        return urlresolvers.reverse(url, args=[url_args])
    else:
        return urlresolvers.reverse(url, args=url_args)


def form_valid_redirection_after_edit(self, form, success_flag, url, url_args=None, form_invalid_flag=False):
    if success_flag:
        return HttpResponseRedirect(self.get_success_url())
    else:
        if form_invalid_flag:
            return self.form_invalid(form)
        else:
            return HttpResponseRedirect(get_failed_url(url, url_args))
