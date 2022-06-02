import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from application.models import Person
from faker import Faker
import dumper
from time import sleep

faker = Faker()

print('')
print("Populating the database...")
print('')
sleep(1)
for _ in range(10):
    fake_name = faker.name()
    person = Person.objects.get_or_create(name=fake_name)[0]
    print('>   ', fake_name)
    sleep(0.02)

sleep(1)
print('')
print('Generation complete')