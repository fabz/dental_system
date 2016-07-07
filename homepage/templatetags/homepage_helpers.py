from datetime import datetime

from django import template
from django.conf import settings
from django.core.urlresolvers import resolve
from django.template.base import TemplateSyntaxError
from django.utils import timezone
from django.utils.timezone import localtime
from django.utils.translation import ugettext
from dentists.models import Specialization
from treatments.models import TreatmentType


register = template.Library()


@register.filter
def in_group(user, group):
    """Returns True/False if the user is in the given group(s).
    Usage::
        {% if user|in_group:"Friends" %}
        or
        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}
    You can specify a single group or comma-delimited list.
    """
    import re
    if re.search(',', group):
        group_list = group.split(',')
    else:
        group_list = [group]
    user_groups = []
    for group in user.groups.all():
        user_groups.append(str(group.name))
    if filter(lambda x: x in user_groups, group_list):
        return True
    else:
        return False
in_group.is_safe = True


@register.filter
def divisible(number, divisor):
    """Returns True/False if the number is divisible by the divisor.
    Usage::
        {% if user|divisible:4 %}
        {% endif %}
    """
    try:
        number = int(number)
        divisor = int(divisor)
        return number % divisor == 0
    except:
        return False
divisible.is_safe = True


@register.simple_tag(takes_context=True)
def override_query(context, key, value):
    """
    return string
    override current query string; add/change one of value
    ex:
        ?username=budi&need_more_food=yes
            command: override_query('username','denvil')
            result: ?username=denvil&need_more_food=yes
    """
    request = context['request']
    current_q = request.GET.copy()
    current_q.__setitem__(key, value)
    return current_q.urlencode()


def get_order_sort(request, field):
    """
    return tupple
    deside field ordering base on field param and order param
    desc:
        of = ordered field
        o  = order type
    ex:
        ?of=username&o=asc
            command: get_order_sort('username')
            result: ('desc', True)
            command: get_order_sort('email')
            result: ('asc', False)
    """
    order = 'asc'
    is_current_field = False
    if 'of' in request.GET:
        current_field = request.GET['of']
        if current_field == field:
            is_current_field = True
            if 'o' in request.GET:
                order = request.GET['o'].lower()
                if order == 'asc':
                    order = 'desc'
                else:
                    order = 'asc'
    return (order, is_current_field)


@register.simple_tag(takes_context=True)
def sort_field_query(context, field):
    """
    return string
    get next ordered field
    ex:
        ?of=username&o=asc
            command: sort_field_query('username')
            result: ?of=username&o=desc
            command: sort_field_query('email')
            result: ?of=email&o=asc
    """
    request = context['request']
    order = get_order_sort(request, field)[0]
    current_q = request.GET.copy()
    current_q.__setitem__('of', field)
    current_q.__setitem__('o', order)
    return current_q.urlencode()


@register.simple_tag(takes_context=True)
def add_export_flag_to_url(context):
    """
    return get paramters string + export_excel flag
    get next ordered field
    ex:
        ?of=username&o=asc
            command: add_export_flag_to_url
            result: ?of=username&o=asc&export_excel=true
    """
    request = context['request']
    current_q = request.GET.copy()
    current_q.__setitem__('export_excel', 'true')
    return current_q.urlencode()


@register.simple_tag(takes_context=True)
def field_sorted(context, field):
    """
    return string
    get arrow icon as field order symbol
    """
    order, is_current_field = get_order_sort(context['request'], field)
    if is_current_field:
        if order == 'asc':
            return '<i class="icon-arrow-up"></i>'
        elif order == 'desc':
            return '<i class="icon-arrow-down"></i>'
    return ''


@register.simple_tag()
def fancy_boolean(value):
    """
    return string
    get fancy boolean symbol
    """
    if value:
        return '<span class="badge badge-success">Y</span>'
    else:
        return '<span class="badge">N</span>'


@register.simple_tag()
def format_time(value):
    """
    return string
    get time formatted seconds
    """
    seconds = int(value)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


@register.simple_tag()
def fancy_message_class(value):
    """
    return string
    get bootstrap alert css class base on django message tags
    """
    if value == 'success':
        return 'alert-success'
    elif value == 'info':
        return 'alert-info'
    elif value == 'error':
        return 'alert-danger'
    else:
        return 'alert'


@register.simple_tag(takes_context=True)
def crud_label(context):
    request = context['request']
    name = resolve(request.path)
    mode = name.url_name.split('_')[-1]
    return ugettext(mode)


@register.filter
def subtract(value, arg):
    return value - (arg or 0)


class SettingsAttrNode(template.Node):

    def __init__(self, variable, default, as_value):
        self.variable = getattr(settings, variable, default)
        self.cxtname = as_value

    def render(self, context):
        context[self.cxtname] = self.variable
        return ''


@register.tag
def get_from_setting(parser, token):
    as_value = variable = default = ''
    bits = token.contents.split()
    if len(bits) == 4 and bits[2] == 'as':
        variable = bits[1]
        as_value = bits[3]
    elif len(bits) == 5 and bits[3] == 'as':
        variable = bits[1]
        default = bits[2]
        as_value = bits[4]
    else:
        raise TemplateSyntaxError("usage: get_from_settings variable default as value "
                                  "OR: get_from_settings variable as value")

    return SettingsAttrNode(variable=variable, default=default, as_value=as_value)


@register.filter
def get_range(value):
    return range(value)


@register.filter
def get_status_view(value):
    return '<span class="glyphicon glyphicon-ok"></span>' if value else '<span class="glyphicon glyphicon-remove"></span>'


@register.filter
def get_treatment_type_view(value):
    return TreatmentType.get_value(TreatmentType, value)


@register.filter
def get_specialization_view(value):
    return Specialization.get_value(Specialization, value)


@register.filter
def get_status_state(value):
    if value == 1:  # Success
        return '<span class="glyphicon glyphicon-ok"></span>'
    elif value == 2:  # On Progress
        return '<span class="fa fa-gear fa-spin"></span>'
    else:  # Failed
        return '<span class="glyphicon glyphicon-remove"></span>'


@register.filter
def get_categories_view(value):
    categories = ""
    if isinstance(value, unicode):
        return value

    for prod_cat, prod_cat_stats, _ in value:
        stats = get_status_view(prod_cat_stats)
        categories += "{} {}\n".format(stats, prod_cat)
    return categories.strip("\n")


@register.filter
def get_product_rank_view(value):
    ranks = ''

    for _, _, rank in value:
        ranks += "{}\n".format(rank)
    return ranks.strip("\n")


@register.filter
def get_rank_view(value):
    ranks = ""
    for rank in value:
        ranks += str(rank.rank) + '\n'
    return ranks.strip("\n")


@register.filter
def convert_unicode_to_date(value):
    return localtime(timezone.make_aware(datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ'), timezone.utc), timezone.get_current_timezone())


@register.filter
def convert_timestamp_to_date(value):
    return datetime.fromtimestamp(int(value) / 1000)
