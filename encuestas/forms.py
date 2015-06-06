from django import forms
from encuestas.models import Persona, CapitalHumano, CapitalFisico, CapitalSocial


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


class CapitalHumano(forms.ModelForm):
    class Meta:
        model = CapitalHumano
        fields = '__all__'


class CapitalFisico(forms.ModelForm):
    class Meta:
        model = CapitalFisico
        fields = '__all__'


class CapitalSocial(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        fields = '__all__'
