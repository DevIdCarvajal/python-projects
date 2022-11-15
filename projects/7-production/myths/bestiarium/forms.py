from django import forms

class CreaturesForm(forms.Form):
  name = forms.CharField(max_length=255, label="Criatura")
  image = forms.CharField(max_length=255, label="Imagen")
  weight = forms.IntegerField(label="Peso")