from datetime import *
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from myutils.models import MarkupMixin 
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

from notes.managers import PublicManager

class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Topic model class.
    """

class Note(MarkupMixin, TimeStampedModel):
    """
    Note model class.

    A simple model to handle adding arbitrary numbers of notes to an animal profile.
    """
    topic=models.models.ForeignKey(Topic)
    date=models.DateField(_('Date'), auto_now=True)
    content=models.TextField(_('Content'))
    rendered_content=models.TextField(_('Rendered content'), blank=True, null=True)
    public=models.BooleanField(_('Public'), default=True)
    author=models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    public_objects = PublicManager()

    class Meta:
        verbose_name=_('Note')
        verbose_name_plural=_('Notes')

    class MarkupOptions:
        rendered_field = 'rendered_content'
        source_field = 'content'
