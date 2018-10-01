from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,Usuario
from . import forms
from first_app.forms import NewUser
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # Aqui se hace un diccionario donde puedes insertar con keys
    # y luego el valor que quieres instertar
    dictionary = {'insert_me':'Hola soy de first app'}
    return render(request,'first_app/clon.html',context=date_dict)
    return render(request,'first_app/clon.html')

def usuarios(request):

    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")

    return render(request,"first_app/crearcuenta.html",{'form':form})
#
# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             #do something code
#             print("validation success!")
#             print("NOMBRE: "+form.cleaned_data['name'])
#             print("EMAIL: "+form.cleaned_data['email'])
#             print("TEXT: "+form.cleaned_data['text'])
#
#     return render(request,'first_app/crearcuenta.html',{'form':form})
