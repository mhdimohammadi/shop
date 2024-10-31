from django import forms
from account.models import ShopUser
from re import match


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=250, widget=forms.PasswordInput, required=True, label='password')
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput, required=True, label='repeat password')

    class Meta:
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Please enter your password correctly ")
        if cd['password2'].isdigit():
            raise forms.ValidationError("password must contain a letter")
        if len(cd['password2']) < 8:
            raise forms.ValidationError("password should be at least 8 character")
        if not bool(match(r'\w*[A-Z]w*', cd['password2'])):
            raise forms.ValidationError("Your password must contain capital letters")
        return cd['password2']
