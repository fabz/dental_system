from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext


class ActiveManager(models.Manager):

    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True, is_deleted=False)


class NotDeletedManager(models.Manager):

    def get_queryset(self):
        return super(NotDeletedManager, self).get_queryset().filter(is_deleted=False)


class DentalModel(models.Model):
    is_active = models.BooleanField(default=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    created_by = models.ForeignKey(User, verbose_name=ugettext('created by'))
    created_time = models.DateTimeField(default=timezone.now, db_index=True)
    modified_by = models.ForeignKey(User, null=True, related_name='+', verbose_name=ugettext('modified by'))
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    active = ActiveManager()
    objects = models.Manager()
    not_deleted = NotDeletedManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #         WARNING!!! CHANGE THIS INTO REAL USER. THIS IS JUST TEMPORARY FOR NO LOGIN.
        self.created_by = User.objects.get(username='system')
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
