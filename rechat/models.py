# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class ChatRoom(models.Model):
    name = models.CharField(max_length=60, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"Slug"))
    groups = models.ManyToManyField(
        Group, blank=True, verbose_name=_(u"Groups"))
    public = models.BooleanField(default=False, verbose_name=_(u"Public room"),
                                 help_text=_(u"All the logged in users can enter this room"))

    class Meta:
        verbose_name = _(u'Chat room')
        verbose_name_plural = _(u'Chat rooms')

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    date = models.DateTimeField(verbose_name=_(u"Date"))
    message = models.TextField(verbose_name=_(u"Message"))
    user = models.ForeignKey(USER_MODEL, null=True, verbose_name=_(u"User"),
                             on_delete=models.SET_NULL)
    room = models.ForeignKey(ChatRoom, null=True, verbose_name=_(u"Room"))

    class Meta:
        verbose_name = _(u'Message')
        verbose_name_plural = _(u'Messages')
        ordering = ['-date']

    def __str__(self):
        return str(self.date)
