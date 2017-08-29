from django.db import models

# Create your models here.
from django.conf import settings
from casino_finder.user_models import User


class Auditable(models.Model):
    created_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    created_by = models.ForeignKey('User', related_name='%(app_label)s_%(class)s_created_by', blank=True, null=True)

    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey('User', related_name='%(app_label)s_%(class)s_modified_by', blank=True, null=True)

    class Meta:
        abstract = True


