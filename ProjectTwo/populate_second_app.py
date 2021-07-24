import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProjectTwo.settings')

import django
django.setup()

from AppTwo.models import user
from faker import Faker

fakeGen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakeGen.name().split()
        first_name=fake_name[0]
        second_name=fake_name[1]
        fake_email=fakeGen.email()

        User=user.objects.get_or_create(firstName=first_name,lastName=second_name,Email=fake_email)[0]

if __name__=='__main__':
    print("populating users")
    populate(20)
    print("completed!!!!")
