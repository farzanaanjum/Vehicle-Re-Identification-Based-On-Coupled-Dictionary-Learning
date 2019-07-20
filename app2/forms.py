from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class Reg(forms.Form):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter your Email','id':'form21' ,'class':'form-control'}))
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'enter your Password', 'id': 'form21', 'class': 'form-control'}))
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter your Name','id':'form21' ,'class':'form-control'}))
    address = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter your Address', 'id': 'form21', 'class': 'form-control'}))
    department = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter your Department', 'id': 'form21', 'class': 'form-control'}))


class Login(forms.Form):
    email = forms.EmailField(max_length=60,widget=forms.TextInput(attrs={'placeholder':'enter your email'}))
    password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'enter your Password'}))
