from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Usuario,Reserva,Reservaciones,Detalle,Asientos,UserProfileInfo
from first_app.forms import UserForm,UserProfileInfoForm
# from first_app.forms import NewUser
# Create your views here.

def index(request):
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records':webpages_list}
    # Aqui se hace un diccionario donde puedes insertar con keys
    # y luego el valor que quieres instertar
    #dictionary = {'insert_me':'Hola soy de first app'}
    #return render(request,'first_app/clon.html',context=date_dict)
    return render(request,'first_app/clon.html')

def reservacion(request):

    status = False

    if status == False:
        status_form = StatusForm(data=request.POST)

        if status_form.is_valid():
            status = status_form.save()
            status = True
        else:
            print(StatusForm.errors)

    else:
        status_form = StatusForm()


def crearcuenta(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app/crearcuenta.html',
                            {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})

def inicio(request):
    return render(request,'first_app/Inicio.html')

# def crearcuenta(request):
#     return render(request,'first_app/crearcuenta.html')

def relative(request):
    return render(request,'first_app/relative_url_templates.html')

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
