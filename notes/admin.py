from notes.models import Note
from django.contrib.contenttypes import generic

class NoteInline(generic.GenericTabularInline):
    model = Note
