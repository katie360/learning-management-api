from django.db import models
from account.models import Account


class Teacher(models.Model):
    username = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20, default='2547xxxxxxxx')
    profile = models.ImageField(blank=True, null=True, upload_to='profile/')
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    subject = models.ManyToManyField("curriculum.Subject", blank=True)
    city = models.CharField(max_length=100, default='Nairobi')
    country = models.CharField(max_length=100, default='Kenya')
    gender = models.CharField(max_length=10)
    dob = models.DateField()

    def __str__(self):
      template = '{0.user.first_name} {0.user.last_name}'
      return template.format(self)
