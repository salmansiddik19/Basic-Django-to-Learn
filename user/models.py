from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db.models import JSONField

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    metadata = models.JSONField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
