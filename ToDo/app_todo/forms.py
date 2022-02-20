from django.forms import ModelForm
from .models import ToDoModel


class ToDoForm(ModelForm):

    class Meta:
        model =ToDoModel
        fields = ['title', 'description', 'important']
