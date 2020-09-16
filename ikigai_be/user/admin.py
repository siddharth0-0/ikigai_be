from django.contrib import admin
from .models import User, Privacy


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('privacy_id', 'privacy_status')


admin.site.register(User)
admin.site.register(Privacy, PrivacyAdmin)