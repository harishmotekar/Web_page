from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "course", "created_at")
    list_filter = ("created_at", "course")
    search_fields = ("name", "email", "course")
    readonly_fields = ("created_at",)
