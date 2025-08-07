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

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'site_name',
                )
            }
        ),
        (
            "icons",
            {
                'fields': (
                    'icon',
                    'favicon'
                )
            }
        ),
        (
            "colors",
            {
                'fields': (
                    'text_color',
                    'main_color',
                    'secondary_color',
                )
            }
        ),
        (
            "navbar",
            {
                'fields': (
                    'sub_navbar_color',
                    'sub_navbar_background_color',
                )
            }
        )
    )
    pass
