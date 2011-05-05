from django.forms import ModelForm
from notes.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields=['content', 'markup', 'topic','date', 'public']
        
class BriefNoteForm(ModelForm):
    class Meta:
        model = Note
        fields=['content', 'topic']
