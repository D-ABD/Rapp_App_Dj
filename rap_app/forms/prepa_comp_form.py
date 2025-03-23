from django import forms
from ..models.prepa_comp import Candidat, Entree, Departement, ObjectifAnnuel


class CandidatForm(forms.ModelForm):
    """Formulaire pour la création et modification d'un candidat"""
    
    class Meta:
        model = Candidat
        fields = ['nom', 'prenom', 'email', 'telephone', 'departement', 'a_adhere']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.Select(attrs={'class': 'form-select'}),
            'a_adhere': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'a_adhere': 'A déjà adhéré au dispositif'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limiter les départements aux codes spécifiés
        departements_codes = ['77', '78', '92', '93', '94', '95']
        self.fields['departement'].queryset = Departement.objects.filter(
            code__in=departements_codes
        )


class EntreeForm(forms.ModelForm):
    """Formulaire pour la création d'une entrée dans le dispositif"""
    
    class Meta:
        model = Entree
        fields = ['candidat', 'departement']
        widgets = {
            'candidat': forms.Select(attrs={'class': 'form-select'}),
            'departement': forms.Select(attrs={'class': 'form-select'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limiter les candidats à ceux qui n'ont pas encore adhéré
        self.fields['candidat'].queryset = Candidat.objects.filter(a_adhere=False)
        # Limiter les départements aux codes spécifiés
        departements_codes = ['77', '78', '92', '93', '94', '95']
        self.fields['departement'].queryset = Departement.objects.filter(
            code__in=departements_codes
        )
        # Rendre le champ candidat optionnel
        self.fields['candidat'].required = False
        self.fields['candidat'].help_text = "Laissez vide pour une entrée directe sans candidature préalable"


class ObjectifAnnuelForm(forms.ModelForm):
    """Formulaire pour modifier l'objectif annuel"""
    
    class Meta:
        model = ObjectifAnnuel
        fields = ['objectif']
        widgets = {
            'objectif': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'objectif': 'Objectif annuel d\'entrées'
        }
        help_texts = {
            'objectif': 'Nombre total d\'entrées à atteindre sur l\'année'
        }