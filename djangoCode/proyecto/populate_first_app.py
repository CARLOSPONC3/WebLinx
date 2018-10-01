import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proyecto.settings')


import django
django.setup()


## Fake pop Script
import random
from first_app.models import AccessRecord,Webpage,Topic,Usuario
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic from the entry
        top = add_topic()

        #Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_nombre = fakegen.first_name()
        fake_apellidoP = fakegen.last_name()
        fake_apellidoM = fakegen.last_name()

        #Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #usuario creado
        usuario = Usuario.objects.get_or_create(nombre=fake_nombre,apellidoP=fake_apellidoP,apellidoM=fake_apellidoM)[0]

        #Create a fake acces record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("Population complete")
