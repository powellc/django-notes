from django import template
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from notes.models import Note

register = template.Library()

def note_list_for(obj):
    """Provides the tags with a "weight" attribute to build a tag cloud"""

    cache_key = 'note_list_for'
    notes = cache.get(cache_key)
    if notes is None:
        # Get all the notes for the specified object
        obj_type=ContentType.objects.get_for_model(obj)
        notes=Note.objects.filter(content_type__pk=obj_type.id, object_id=obj.id)

        if len(notes) == 0:
            # go no further
            return {}
        cache.set(cache_key, notes)

    return {'notes': notes}

register.inclusion_tag('notes/_note_list.html')(note_list_for) 
