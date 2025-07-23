# coding=utf-8

import os

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models

from .singleton import SingletonModel  # noqa


def validate_svg_or_image(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ['.svg', '.png', '.jpg', '.jpeg', '.gif', '.ico']:
        raise ValidationError(
            'Unsupported file type. Allowed: SVG, PNG, JPG, JPEG, GIF, ICO.')


class SitePreferences(SingletonModel):
    """Preference settings for project."""

    favicon = models.FileField(
        upload_to='site-preferences',
        null=True,
        blank=True,
        help_text=(
            'Upload an image file (.ico) to be used as favicon.'
            'The default is kartoza icon'
        ),
        validators=[validate_svg_or_image]
    )

    icon = models.FileField(
        upload_to='site-preferences',
        null=True,
        blank=True,
        help_text=(
            'Upload an image file to be used as icon on navbar.'
            'The default is kartoza.ico'
        ),
        validators=[validate_svg_or_image]
    )

    main_color = ColorField(
        null=True,
        blank=True,
        help_text=(
            'Choose the main color for the site.'
            'Default is Kartoza blue'
        )
    )

    site_name = models.TextField(
        null=True,
        blank=True,
        default='Kartoza GeoNode',
        help_text=(
            'Choose the site name for navbar and on banners.'
        )
    )

    class Meta:  # noqa: D106
        verbose_name_plural = "site preferences"
