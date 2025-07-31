from django import forms

class ParticipationForm(forms.Form):
    first_name = forms.CharField(label="İsim", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Soyisim", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-posta", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label="Çekiliş Kodu", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))