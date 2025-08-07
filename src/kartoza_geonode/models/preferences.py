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

    # -------------------------------------
    # ICONS
    # -------------------------------------
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

    # -------------------------------------
    # COLORS
    # -------------------------------------
    text_color = ColorField(
        default='#3E3E3E',
        help_text=(
            'Choose the text color for the site.'
        )
    )

    main_color = ColorField(
        default='#57A0C7',
        help_text=(
            'Choose the main color for the site.'
        )
    )

    secondary_color = ColorField(
        default='#ECB44B',
        help_text=(
            'Choose the secondary color for the site.'
        )
    )

    # -------------------------------------
    # NAVBAR
    # -------------------------------------
    sub_navbar_color = ColorField(
        default='#FFFFFF',
        help_text=(
            'Choose the text color for the sub navbar.'
        )
    )

    sub_navbar_background_color = ColorField(
        default='#57A0C7',
        help_text=(
            'Choose the background color for the sub navbar.'
        )
    )

    site_name = models.TextField(
        default='GeoNode',
        help_text=(
            'Choose the site name for navbar and on banners.'
        )
    )

    class Meta:  # noqa: D106
        verbose_name_plural = "site preferences"
