from django.db import models


class CodeField(models.CharField):
    description = "Code field"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 40)
        super(CodeField, self).__init__(*args, **kwargs)


class NameField(models.CharField):
    description = "Name field"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 70)
        super(NameField, self).__init__(*args, **kwargs)
