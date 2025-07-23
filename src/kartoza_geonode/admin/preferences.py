# coding=utf-8

from django.contrib import admin
from django.contrib.admin.sites import NotRegistered

from kartoza_geonode.models.preferences import SitePreferences

try:
    admin.site.unregister(SitePreferences)
except NotRegistered:
    pass


@admin.register(SitePreferences)
class SitePreferencesAdmin(admin.ModelAdmin):
    """SitePreferences Admin."""

    pass
