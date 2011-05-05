from datetime import *
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from markup_mixin.models import MarkupMixin 
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

from notes.managers import PublicManager

class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Topic model class.
    """

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __unicode__(self):
        return self.title

class Note(MarkupMixin, TimeStampedModel):
    """
    Note model class.

    A simple model to handle adding arbitrary numbers of notes to an animal profile.
    """
    topic=models.ForeignKey(Topic)
    date=models.DateField(_('Date'), default=datetime.now())
    content=models.TextField(_('Content'))
    rendered_content=models.TextField(_('Rendered content'), blank=True, null=True, editable=False)
    public=models.BooleanField(_('Public'), default=True)
    author=models.ForeignKey(User, blank=True, null=True)
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
        

