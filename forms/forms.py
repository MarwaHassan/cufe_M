from django import forms
from filer.fields.file import FilerFileField
from django.db import models

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    disclaimer = FilerFileField(null=True, blank=True,
                                related_name="disclaimer_company",
                                on_delete=models.CASCADE)
    # file = forms.FileField()
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={#'multiple': True,
    #                                                                     'class': 'file-upload',
    #                                                                     }))
