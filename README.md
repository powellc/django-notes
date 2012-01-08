django-notes
=============

A simple application to allow you to attach notes to models.

Installation
-------------

Notes uses generic relations to handle attaching themselves to models. So installation is basically just like adding a generic relation item to your model.

1. Add 'notes' to your INSTALLED_APPS variable
2. Import the Note model:

        from notes.models import Note

3. Add the note inline to your model's admin def in your admin.py file:

        from notes.admin import NoteInline

        class YourModelAdmin(admin.ModelAdmin):
            inlines = [ NoteInline, ]
        
4. To enable easy management you can add a hook to your model:

        notes=generic.GenericRelation(Note)

Usage
------
Follow the steps above (including 4) and you should have access to all the notes at instance_of_yourmodel.notes_set.all():

    >>> object = YourModel.objects.get(pk=1)
    >>> notes_for_object = object.notes_set.all()

Simple.
