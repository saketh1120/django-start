import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from first_app.models import Users
from faker import Faker
fake_gen = Faker()

def populate(N=10):
    for i in range(N):
        first_name = fake_gen.name().split(" ")[0]
        last_name = fake_gen.name().split(" ")[1]
        email_id = fake_gen.email()
        users = Users.objects.get_or_create(first_name=first_name, last_name=last_name, email_id=email_id)[0]


if __name__ == "__main__":
    print("populating users")
    populate(5)
    print("populated users!")
else:
    populate(10)
