from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserInfo(models.Model):
    first_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name


class UserProfileUpdate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    # additional classes
    user_portfolio = models.URLField(blank=True)
    user_image = models.ImageField(upload_to="profile_pic", blank=True)


    def __str__(self):
        return self.user.username


