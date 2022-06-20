from django import forms
from .models import VolunteerRegistrationModel


class VolunteerRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(),
                           required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(
        attrs={'pattern': '[a-zA-Z0-9]+'}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                                                                 'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
                               required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}'}), required=True,
                             max_length=100)
    email = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}),
                            required=True, max_length=100)
    ward = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[0-9]'}), required=True,
                           max_length=100)

    class Meta():
        model = VolunteerRegistrationModel
        fields = [
            'name',
            'loginid',
            'password',
            'mobile',
            'email',
            'ward'
        ]
