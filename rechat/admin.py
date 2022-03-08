from django.contrib import admin

from .models import ChatMessage, ChatRoom


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    readonly_fields = ["date"]
    list_display = ["date", "user"]
    list_filter = (("user", admin.RelatedOnlyFieldListFilter),)
    filters_on_top = True
    list_select_related = ("user",)


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "save_messages"]
    prepopulated_fields = {
        "slug": ("name",),
    }
