from django.db import models


# Create your models here.
class VolunteerRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'VolunteerRegistrations'
