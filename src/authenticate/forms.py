from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class PasswordChangeform(PasswordChangeForm):

    class Meta:
        model = User
        fields = (
            'old_password', 'new_password1', 'new_password2'
        )

    def __init__(self, *args, **kwargs):
        super(PasswordChangeform, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

        self.fields['old_password'].label = ""
        self.fields['new_password1'].label = ""
        self.fields['new_password2'].label = ""

        self.fields['old_password'].widget.attrs['placeholder'] = 'Write old password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Write new password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm password'

        self.fields['new_password1'].help_text = """<ul class='form-text text-muted small'>
                                                        <li>Your password can\'t be too similar to your other personal information.</li>
                                                        <li>Your password must contain at least 8 characters.</li>
                                                        <li>Your password can\'t be a commonly used password.</li>
                                                        <li>Your password can\'t be entirely numeric.</li>
                                                        </ul>"""


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password'
        )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Lastname'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'

        self.fields['username'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""

        self.fields['username'].help_text = """<span class='form-text text-muted'><small>
                                                Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
                                            </small></span>"""



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                         'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
                                                                                        'placeholder': 'Enter Lastname'}))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Enter UserName'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""

        self.fields['username'].help_text = "<span class='form-text text-muted'><small>" \
                                            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only." \
                                            "</small></span>"

        self.fields['password1'].help_text = """<ul class='form-text text-muted small'>
                                                <li>Your password can\'t be too similar to your other personal information.</li>
                                                <li>Your password must contain at least 8 characters.</li>
                                                <li>Your password can\'t be a commonly used password.</li>
                                                <li>Your password can\'t be entirely numeric.</li>
                                                </ul>"""

        self.fields['password2'].help_text = "<span class='form-text text-muted'><small>" \
                                             "Enter the same password as before, for verification." \
                                             "</small></span>"
