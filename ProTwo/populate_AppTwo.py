import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

##fake pop Script
from AppTwo.models import User
from faker import Faker

fakegen = Faker()





def populate(N=100):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_FirstName = fake_name[0]
        fake_LastName = fake_name[1]
        fake_email = fakegen.email()

        users = User.objects.get_or_create(FirstName=fake_FirstName,LastName=fake_LastName, Email=fake_email)[0]







if __name__ == '__main__':
    print("populating script!")
    populate()
    print("populating complete!")
