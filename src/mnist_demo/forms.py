from io import BytesIO

from django import forms
from django.core.files import File
from PIL import Image


class UploadImageForm(forms.Form):
    image = forms.ImageField(
        label='Загрузите картинку',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'id': 'FormFile'
        })
    )

    # def clean_image(self):
    #     image = Image.open(self.cleaned_data['image'])
    #     if image.size != (28, 28):
    #         image.resize((28, 28))
    #         image_io = BytesIO()
    #         image.save(image_io, 'JPEG', quality=100)
    #     return File(image_io, name=image.name)
