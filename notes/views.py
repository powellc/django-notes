from django.views.generic import ListView, DetailView

from notes.models import Note

class NoteList(ListView):
    model = Note

    def get_queryset(self):
        if self.request.user.is_authenticated: qs = Note.objects.order_by("-date")
        else: qs = Note.public_objects.order_by("-date")
        return qs

    def get_context_data(self, **kwargs):
        context = super(NoteList, self).get_context_data(**kwargs)
        context['topic_list']=Topic.objects.all()
        return context

class NoteDetail(DetailView):
    model = Note

    def get_queryset(self):
        if self.request.user.is_authenticated: qs = Note.objects.order_by("-date")
        else: qs = Note.public_objects.order_by("-date")
        return qs
