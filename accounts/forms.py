from django import forms


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))  # User cant change the username
    password = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
