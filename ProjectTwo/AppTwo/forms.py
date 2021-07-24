from django import forms
from django import forms
from AppTwo.models import user

class myNewUser(forms.ModelForm):

    class Meta():
        model=user
        fields='__all__'