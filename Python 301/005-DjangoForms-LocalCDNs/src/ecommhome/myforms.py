# import forms from django
from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

# create a form class ingerited from forms.Form for Contact Form
class ContactForm(forms.Form):
    # define the form fields and there widget details - reference this URL - https://docs.djangoproject.com/en/3.0/ref/forms/fields/
    contactname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter contact name'}))
    emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'please enter email id'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'please enter address'}))

    # define the validation per field ....
    # its uses a keyword 'clean_' + fieldname to define a validation for the field
    def clean_emailid(self):
        emailId = self.cleaned_data.get('emailid')
        if not '@gmail.com' in emailId:
            # raise an error 
            raise forms.ValidationError('Email has to be gmail.com.')
        return emailId

# create a form class ingerited from forms.Form for Login Form
class LoginForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter username'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'please enter password'}))

# create a form class ingerited from forms.Form for Register Form
class RegisterForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter username'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'please enter password'}))
     passwordretype = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'please re-enter password'}))
     emailId = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'please enter email id'}))

     def clean_username(self):
         username = self.cleaned_data.get('username')
         user = User.objects.filter(username=username)
         if user.exists():
             raise forms.ValidationError("User Name Already Exists.")
         return username

     def clean_emailId(self):
         emailid = self.cleaned_data.get('emailId')
         email = User.objects.filter(email=emailid)
         if email.exists():
             raise forms.ValidationError("Email ID Already Exists.")
         return emailid
     
     def clean(self):
         formmdata = self.cleaned_data
         password = self.cleaned_data.get('password')
         passwordretype = self.cleaned_data.get('passwordretype')
         if password != passwordretype :
             raise forms.ValidationError("Passwords don't match.")
         return formmdata