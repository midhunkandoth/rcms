from django import forms
from django.forms import ModelForm
from models import PartsArrangement


class PartsArrangementForm(ModelForm):

    class Meta:
        model = PartsArrangement