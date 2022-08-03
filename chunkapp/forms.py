from dataclasses import fields
from django import forms
from . utils import validateFile
from . models import ChunkOrder
from django.forms import ModelForm


# this is the form that takes in the required entries to chunk a file
# the file to be chunked is also uploaded within this form along with
# the size of chunks
# class ChunkOrderForm(forms.Form):
#     # the file field is for the file that is to be uploaded
#     # the chunk size is to determine how the file is going to be chunked
#     file = forms.FileField(validators=[validateFile])
#     chunk_size = forms.IntegerField()

class FileUploadForm(ModelForm):
    class Meta:
        model=ChunkOrder
        fields=['file']

class ChunkSizeForm(ModelForm):
    class Meta:
        model=ChunkOrder
        fields=['chunk_size']

