from django.contrib import admin

from .models import Gift, Guest, Party


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
