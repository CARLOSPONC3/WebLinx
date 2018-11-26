from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from first_app.models import Usuario,Reserva,Reservaciones,Asientos,UserProfileInfo
from first_app.forms import UserForm,UserProfileInfoForm,StatusForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
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

@login_required
def user_logout(request):
    logout(request)
    return render(request,"first_app/Inicio.html")
    # return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Has iniciado sesión correctamente!")

def selmesa(request):
    smesa = request.POST.get('mesa')
    asientos = Asientos.objects.filter(mesa=bar)
    return smesa



def reservacion(request):
    #bar=selmesa(request)
    asientos = Asientos.objects.all()#mesa=bar)
    asien = [request.POST.get('este')]
    for i in asien:
        if request.method == "POST":
            estatus = Asientos.objects.get(asiento=i)
            if estatus.status == True:
                estatus.status = False
            else:
                estatus.status = True
            estatus.save()

    return render(request,"first_app/reservacion.html", {'asientos': asientos})


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


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,"first_app/Inicio.html")
                # return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("CUENTA NO ACTIVADA")
        else:
            print("Alguien intento ingresar pero no pudo")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Datos no validos!")
    else:
        return render(request,'first_app/user_login.html',{})


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
