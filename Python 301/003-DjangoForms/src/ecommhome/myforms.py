# import forms from django
from django import forms

# create a form class ingerited from forms.Form
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