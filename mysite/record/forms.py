from django import forms

from .models import Plant, Post


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ('user', 'plant_name', 'plant_text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('created_date', 'plant_height', 'description',)
