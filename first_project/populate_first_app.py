import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
#
import django

django.setup()

# fake population script

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake_gen = Faker()
topics = ["Search", "News", "Games", "Weather", "Score"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        #   get the topic for entry
        top = add_topic()
        # create fake daa for thr topic
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        #   create the new webpage entry
        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print("populate script!")
    populate(20)
    print("populating complete!")
