from django import forms
from django.core import validators
from first_app.models import Usuario

#validacion custom para lo que requiera en este caso z de inicio de nombre
    # if value[0].lower() != 'z':
    #     raise forms.ValidationError("Name needs to start with z")

class NewUser(forms.ModelForm):
    class Meta():
        model = Usuario
        fields = '__all__'

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifique_email = forms.EmailField(label='Ingrese su email nuevamente')
    text = forms.CharField(widget = forms.Textarea)
    # botcacther = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifique_email']

        if email != vmail:
            raise forms.ValidationError("Asegurese que los emails son iguales")



# #manual no necesaria
#     def clean_botcatcher(self):
#         botcatcher = self.cleaned_data['botcatcher']
#         if len(botcatcher) > 0:
#             raise forms.ValidationError("Gotcha Bot!")
#         return botcatcher
