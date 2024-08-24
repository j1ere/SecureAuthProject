from django import forms
from .models import CustomUserModel, RegistrationDetails

#admin form registration
class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationDetails
        fields = ['full_names', 'hostel_name', 'phone_number']

#user account creation form
class UserAccountCreation(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput)
    confirm_password = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords Do Not Match')
        
        return cleaned_data