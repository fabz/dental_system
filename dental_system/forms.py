from django import forms


class SearchForm(forms.Form):
    advanced_search_index = 0  # start at 1, because of has_search hidden field
    has_search = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    view = None

    def __init__(self, *args, **kwargs):
        self.view = kwargs.pop('view_object', None)
        super(forms.Form, self).__init__(*args, **kwargs)
        self.is_bound = True

    def prepare_initial_data(self, data):
        data.__setitem__('has_search', '1')
        return data

    def get_query_string(self):
        return ''
