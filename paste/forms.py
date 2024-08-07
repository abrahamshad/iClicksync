from django import forms
from .models import Paste, EXPIRATION_CHOICES
from django.core.exceptions import ValidationError
# from django_summernote.widgets import SummernoteWidget


class PasteForm(forms.ModelForm):
    expiration_time = forms.ChoiceField(choices=EXPIRATION_CHOICES, label='expiration time')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='password (optional)')
    file = forms.FileField(required=False, label='file (optional)')
    # content = forms.CharField(widget=SummernoteWidget())


    class Meta:
        model = Paste
        fields = ['title', 'content', 'expiration_time', 'password', 'file']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            allowed_formats = [
                'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso',
                'arj', 'lzh', 'cab', 'tgz', 'tbz2'
            ]
            file_extension = file.name.split('.')[-1].lower()
            if file_extension not in allowed_formats:
                raise ValidationError("The file format should be one of these:" + ", ".join(allowed_formats))
        return file