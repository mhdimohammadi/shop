from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone already exist')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('phone already exist')
        if not phone.isdigit():
            raise forms.ValidationError('phone must be a number')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone must starts with 09 digit')
        if len(phone) != 11:
            raise forms.ValidationError('phone must be 11 digits')
        return phone


class ShopUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone already exist')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('phone already exist')
        if not phone.isdigit():
            raise forms.ValidationError('phone must be a number')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone must starts with 09 digit')
        if len(phone) != 11:
            raise forms.ValidationError('phone must be 11 digits')
        return phone
