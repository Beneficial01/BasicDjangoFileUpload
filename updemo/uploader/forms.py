from django import forms
from .models import SampleFile

class SampleFileForm(forms.ModelForm):
    class Meta:
        model = SampleFile
        fields = ('sample_id', 'file')