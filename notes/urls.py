from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, EditView
from notes.models import Note, Topic

from notes.views import NoteList, NoteDetail

urlpatterns = patterns('',
    url(r'^$', NoteList.as_view(), name='notes-index'),
    url(r'^add/$', login_required(CreateView.as_view(model=Note), name='notes-create')),
    url('^(?P<pk>\d+)/$', NoteDetail.as_view(), name='notes-view'),
    url('^(?P<pk>\d+)/edit/$', login_required(EditView.as_view(model=Note)), name='notes-edit'),
)
