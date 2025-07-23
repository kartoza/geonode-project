# coding=utf-8

from rest_framework import serializers

from kartoza_geonode.models.preferences import SitePreferences


class SitePreferencesSerializer(serializers.ModelSerializer):
    """Site preference serializer."""

    icon = serializers.SerializerMethodField()
    favicon = serializers.SerializerMethodField()

    def get_icon(self, obj: SitePreferences):
        """Return icon."""
        return obj.icon.url if obj.icon else ''

    def get_favicon(self, obj: SitePreferences):
        """Return favicon."""
        return obj.favicon.url if obj.favicon else ''

    class Meta:  # noqa: D106
        model = SitePreferences
        exclude = ()
