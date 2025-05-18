from django import forms
from myapp.models import Contatto 

class ContattoForm(forms.ModelForm):
    telefono = forms.CharField(
        min_length=10,
        error_messages={
            'min_length': 'Il numero deve essere lungo esattamente 10 cifre.',           
        },
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Contatto
        fields = ['nome', 'cognome', 'telefono']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("Il numero di telefono deve contenere solo cifre.")
        
        qs = Contatto.objects.filter(telefono=telefono)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Questo numero è già presente in rubrica.")
        return telefono
    