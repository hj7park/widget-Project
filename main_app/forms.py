from django.forms import ModelForm
from .models import Widget


class widgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description','quantity']