from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
# from django.core.exceptions import ValidationError  
from django.forms import inlineformset_factory
from django.forms import formset_factory



class UserRegistrationForm(forms.ModelForm):

    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        ordering = ['first_name']
        # fields = "__all__"
        fields = ('first_name', 'last_name','username', 'email', 'password', 'password2')
        help_texts = {
            'username': None
        }
        widgets = {
            'password' : forms.PasswordInput,
        }

    def clean(self):
        pass

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

        

# Authenticate User Form
class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserInformationForm(forms.ModelForm):
    skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget = forms.CheckboxSelectMultiple())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'profile_pic', 'username', 'address', 'contact', 'birth_date', 'gender', 'skill', 'language')
        help_texts = {
            "username": None
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'class':'form-control', 'format': 'yyyy-mm-dd','type':'date'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER, attrs={'class': 'form-control'}),
        }

class UserEducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('name', 'location', 'level', 'grade', 'enroll_date', 'passed_date')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'level':forms.Select(choices=TYPE, attrs={'class':'form-control'}),
            'grade':forms.NumberInput(attrs={'class':'form-control'}),
            'enroll_date':forms.DateInput(attrs={'class':'form-control', 'format': 'yyyy-mm-dd','type':'date'}),
            'passed_date':forms.DateInput(attrs={'class':'form-control', 'format': 'yyyy-mm-dd','type':'date'})
        }
EducationFormSet = inlineformset_factory(CustomUser, Education, form=UserEducationForm, extra=1)


class UserWorkForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'location' : forms.TextInput(attrs={'class' : 'form-control'}),
            'joined_date' : forms.DateInput(attrs={'class' : 'form-control', 'format' : 'yyyy-mm-dd', 'type' : 'date'}),
            'left_date' : forms.DateInput(attrs={'class' : 'form-control', 'format' : 'yyyy-mm-dd', 'type' : 'date'})
        }
WorkFormSet = inlineformset_factory(CustomUser, Company, form = UserWorkForm, extra=1)


class UserAchievementForm(forms.ModelForm):

    class Meta:
        model = Achievement
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'platform_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '5'}),
            'duration' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
AchievementFormset = inlineformset_factory(CustomUser, Achievement, form = UserAchievementForm, extra = 1)


class UserLinkForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'github' : forms.URLInput(attrs={'class' : 'form-control'}),
            'linkedin' : forms.URLInput(attrs={'class' : 'form-control'}),
            'instagram' : forms.URLInput(attrs={'class' : 'form-control'}),
            'aboutme' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '5'}),
        }
LinkFormSet = inlineformset_factory(CustomUser, PersonalInfo, form = UserLinkForm, extra=1)


class UserReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'reference_description' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '5'})
        }
ReferenceFormSet = inlineformset_factory(CustomUser, Reference, form = UserReferenceForm, extra=1)


class UserSkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class UserLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }