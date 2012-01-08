from notes.models import Note, Topic
from django.contrib import admin
from django.contrib.contenttypes import generic

class NoteInline(generic.GenericTabularInline):
    model = Note

admin.site.register(Topic)
admin.site.register(Note)
