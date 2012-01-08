.. _usage:

Usage
=====

Follow the steps above (including 4) and you should have access to all the notes at instance_of_yourmodel.notes_set.all():

> object = YourModel.objects.get(pk=1)
> notes_for_object = object.notes_set.all()

Simple.

