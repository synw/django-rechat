# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class ChatMessage(models.Model):
    date = models.DateTimeField(verbose_name=_(u"Date"))
    message = models.TextField(verbose_name=_(u"Message"))
    user = models.ForeignKey(USER_MODEL, null=True, verbose_name=_(u"User"),
                             on_delete=models.SET_NULL)

    class Meta:
        app_label = 'rechat'
        verbose_name = _(u'Message')
        verbose_name_plural = _(u'Messages')
        ordering = ['-date']

    def __str__(self):
        return str(self.date)
