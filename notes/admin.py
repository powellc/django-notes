from notes.models import Note, Topic
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

class NoteInline(GenericTabularInline):
    model = Note

admin.site.register(Topic)
admin.site.register(Note)
