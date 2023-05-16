from django import forms
from .models import *

class EquipmentListForm(forms.ModelForm):
    class Meta:
        model = EquipmentList
        fields = "__all__"

        widgets = {
            "equipmentId":forms.Select(attrs={"class":"form-control mb-2"}),
            "specificationId":forms.Select(attrs={"class":"form-control mb-2"}),
            "fileName":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "fileImage":forms.FileInput(attrs={"class":"form-control mb-2"})
        }