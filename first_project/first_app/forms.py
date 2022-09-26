from django import forms
from django.core import validators
from .models import AccessRecord,Webpage,Topic,UserInfo, UserProfileUpdate
from django.contrib.auth.models import User


class MyNewForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = "__all__"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # user_url = forms.URLField(label="Update the profile URL here")
    # user_image = forms.ImageField(label="Update your profile image here")

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileUpdate
        fields = ("user_portfolio", "user_image")








# custom validators need an keyword argument("value") this tells django that it is a validator.
# This is for a single check.
def check_for_a(value):
    if value[0].lower() != "a":
        raise forms.ValidationError("Name should start with a")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    # cake = forms.DateField(widget=forms.DateInput)
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    Remarks = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])







    # To clean check all the form at once we can do this:
    def clean(self):
        all_clean_data = super(FormName, self).clean()
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError("Email dont match.")


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #
    #     return botcatcher