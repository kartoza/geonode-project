# coding=utf-8

from django.db import models

from .singleton import SingletonModel  # noqa


class SitePreferences(SingletonModel):
    """Preference settings for project."""

    favicon = models.ImageField(
        upload_to='site-preferences',
        null=True,
        blank=True,
        help_text=(
            'Upload an image file (.ico) to be used as favicon.'
            'The default is kartoza icon'
        )
    )

    icon = models.ImageField(
        upload_to='site-preferences',
        null=True,
        blank=True,
        help_text=(
            'Upload an image file to be used as icon on navbar.'
            'The default is kartoza.ico'
        )
    )

    class Meta:  # noqa: D106
        verbose_name_plural = "site preferences"
