from collections import OrderedDict

from django import forms



class Client(forms.Form):
    nom = forms.CharField(max_length=30, help_text="Votre Nom", required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(max_length=30, help_text="Votre Prénom", required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    telephone = forms.CharField(max_length=10, help_text="Votre numéro de Téléphone", required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    commune = forms.ChoiceField(choices=[('Bandalungwa', 'Bandalungwa'), ('Barumbu', 'Barumbu'), ('Bumbu', 'Bumbu'),
                                         ('Gombe', 'Gombe'), ('Kalamu', 'Kalamu'), ('Kasa-vubu', 'Kasa-vubu'),
                                         ('Kimbaseke', 'Kimbaseke'),
                                         ('Kinshasa', 'Kinshasa'), ('Kintambo', 'Kintambo'), ('Kisenso', 'Kisenso'),
                                         ('Lemba', 'Lemba'),
                                         ('Limete', 'Limete'), ('Lingwala', 'Lingwala'), ('Makala', 'Makala'),
                                         ('Maluku', 'Maluku'),
                                         ('Masina', 'Masina'), ('Matete', 'Matete'), ('Mont-ngafula', 'Mont-ngafula'),
                                         ('N\'djili', 'N\'djili'),
                                         ('Ngaba', 'Ngaba'), ('Ngaliema', 'Ngaliema'), ('Ngiri-ngiri', 'Ngiri-ngiri'),
                                         ('N\'sele', 'N\'sele'), ('Selembao', 'Selembao')],
                                help_text="Choisissez votre Commune",
                                widget=forms.Select(attrs={'class': 'form-control'}))
    adresse = forms.CharField(max_length=30, help_text="Votre Adresse", required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        nom.replace(" ", "")
        if len(nom) < 2:
            raise forms.ValidationError("*Ce nom est trop court !")

        return nom

    def clean_adresse(self):
        adresse = self.cleaned_data['adresse']
        adresse.replace(" ", "")
        if len(adresse) < 6:
            raise forms.ValidationError("*Cette adresse n'a pas assez d'information!")

        return adresse

    def clean_commune(self):
        commune = self.cleaned_data['commune']
        commune.replace(" ", "")
        if len(commune) < 5:
            raise forms.ValidationError("*Le nom de la commune trop court !")

        return commune

    def clean_prenom(self):

        prenom = self.cleaned_data['prenom']
        prenom.replace(" ", "")
        if len(prenom) < 2:
            raise forms.ValidationError("*Ce prenom est trop court !")

        return prenom

    def clean_telephone(self):

        telephone = self.cleaned_data['telephone']
        telephone.replace(" ", "")
        if len(telephone) != 10:
            raise forms.ValidationError("*Ce numéro est trop court !")
        # if  telephone not numeric:
        #   raise forms.ValidationError("*Caractere incorrect !")
        a = telephone[0] + telephone[1] + telephone[2]
        LesCodeNumero = ['081', '082', '089', '085', '084', '090', '097', '099']
        if a not in LesCodeNumero:
            raise forms.ValidationError("*Le numéro n'est pas valide !")

        b = User.objects.filter(username=telephone)
        if b:
            raise forms.ValidationError("*Ce numéro est deja utilisé !")

        return telephone


class Reservation(forms.Form):
    nom = forms.CharField(max_length=30, help_text="Son Nom", required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(max_length=30, help_text="Son Prénom", required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(help_text="Son adresse email", required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(max_length=10, help_text="Son numéro de Téléphone", required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    commune = forms.ChoiceField(choices=[('Bandalungwa', 'Bandalungwa'), ('Barumbu', 'Barumbu'), ('Bumbu', 'Bumbu'),
                                         ('Gombe', 'Gombe'), ('Kalamu', 'Kalamu'), ('Kasa-vubu', 'Kasa-vubu'),
                                         ('Kimbaseke', 'Kimbaseke'),
                                         ('Kinshasa', 'Kinshasa'), ('Kintambo', 'Kintambo'), ('Kisenso', 'Kisenso'),
                                         ('Lemba', 'Lemba'),
                                         ('Limete', 'Limete'), ('Lingwala', 'Lingwala'), ('Makala', 'Makala'),
                                         ('Maluku', 'Maluku'),
                                         ('Masina', 'Masina'), ('Matete', 'Matete'), ('Mont-ngafula', 'Mont-ngafula'),
                                         ('N\'djili', 'N\'djili'),
                                         ('Ngaba', 'Ngaba'), ('Ngaliema', 'Ngaliema'), ('Ngiri-ngiri', 'Ngiri-ngiri'),
                                         ('N\'sele', 'N\'sele'), ('Selembao', 'Selembao')],
                                help_text="Choisissez votre Commune",
                                widget=forms.Select(attrs={'class': 'form-control'}))
    adresse = forms.CharField(max_length=30, help_text="Son Adresse", required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_nom(self):
        nom = self.cleaned_data['nom']
        nom.replace(" ", "")
        if len(nom) < 2:
            raise forms.ValidationError("*Ce nom est trop court !")

        return nom

    def clean_adresse(self):
        adresse = self.cleaned_data['adresse']
        adresse.replace(" ", "")
        if len(adresse) < 6:
            raise forms.ValidationError("*Cette adresse n'a pas assez d'information!")

        return adresse

    def clean_commune(self):
        commune = self.cleaned_data['commune']
        commune.replace(" ", "")
        if len(commune) < 5:
            raise forms.ValidationError("*Le nom de la commune trop court !")

        return commune

    def clean_prenom(self):

        prenom = self.cleaned_data['prenom']
        prenom.replace(" ", "")
        if len(prenom) < 2:
            raise forms.ValidationError("*Ce prenom est trop court !")

        return prenom

    def clean_telephone(self):

        telephone = self.cleaned_data['telephone']
        telephone.replace(" ", "")
        if len(telephone) != 10:
            raise forms.ValidationError("*Ce numéro est trop court !")
        # if  telephone not numeric:
        #   raise forms.ValidationError("*Caractere incorrect !")
        a = telephone[0] + telephone[1] + telephone[2]
        LesCodeNumero = ['081', '082', '089', '085', '084', '090', '097', '099']
        if a not in LesCodeNumero:
            raise forms.ValidationError("*Le numéro n'est pas valide !")

        b = User.objects.filter(username=telephone)
        if b:
            raise forms.ValidationError("*Ce numéro est deja utilisé !")

        return telephone

    def clean_email(self):

        email = self.cleaned_data['email']
        email.replace(" ", "")

        b = User.objects.filter(email=email)
        if b:
            raise forms.ValidationError("*Ce email est deja utilisé !")

        return email
