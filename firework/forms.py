from django import forms
from .models import TablesFire, FirePosition

class TablesFireAdminForm(forms.ModelForm):
   

    class Meta:
        model = TablesFire
        fields = '__all__'

class FirePositionAdminForm(forms.ModelForm):
   

    class Meta:
        model = FirePosition
        fields = '__all__'
