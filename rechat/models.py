from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from instant.models import Channel, LEVELS

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", User)


class ChatRoom(models.Model):
    name = models.CharField(max_length=60, verbose_name=_("Name"))
    slug = models.SlugField(verbose_name=_("Slug"), unique=True)
    level = models.CharField(
        max_length=20, choices=LEVELS, verbose_name=_("Authorized for")
    )
    groups = models.ManyToManyField(Group, blank=True, verbose_name=_("Groups"))
    channel = models.ForeignKey(
        Channel,
        verbose_name=_("Channel"),
        null=True,
        editable=False,
        blank=True,
        on_delete=models.PROTECT,
    )
    save_messages = models.BooleanField(verbose_name=_("Save messages"), default=True)

    class Meta:
        verbose_name = _("Chat room")
        verbose_name_plural = _("Chat rooms")

    @property
    def channel_name(self) -> str:
        return self.channel.name

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    date = models.DateTimeField(verbose_name=_("Date"), auto_now=True)
    message = models.TextField(verbose_name=_("Message"))
    user = models.ForeignKey(
        USER_MODEL, null=True, verbose_name=_("User"), on_delete=models.SET_NULL
    )
    room = models.ForeignKey(
        ChatRoom, null=True, verbose_name=_("Room"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ["-date"]

    def __str__(self):
        return str(self.date)
