.. _installation:

Installation
============

* To install ::

    pip install django-notes

* Add ``''`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        "notes",
        ...
    )

* Import the Note model in your model::

    from notes.models import Note

* Add the note inline to your model's admin def in your admin.py file::

    from notes.admin import NoteInline

    class YourModelAdmin(admin.ModelAdmin):
        inlines = [ NoteInline, ]
        
* To enable easy management you can add a hook to your model::

    notes=generic.GenericRelation(Note)

* Finally, if you want to handle/view notes by themselves::
  
    urlpatterns += patterns('',
        ...  
        (r'^', include('farm.urls')),
        ...
    )


