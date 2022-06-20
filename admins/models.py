from django.db import models
from Volunteers.models import VolunteerRegistrationModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


def mobileNoValidate(mobileNo):
    if mobileNo < 5999999999 & mobileNo > 9999999999:
        raise ValidationError(
            _('%(value)s is not an even number'), params={'value': value},
        )


class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(help_text='yyyy-mm-dd')
    mobileNo = models.IntegerField(
        max_length=10, validators=[mobileNoValidate])
    aadharNo = models.IntegerField(max_length=12, unique=True)
    rationNo = models.CharField(max_length=10)
    pan = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    wardNo = models.IntegerField()
    volunteer = models.ForeignKey(
        VolunteerRegistrationModel, on_delete=models.CASCADE)


class Services(models.Model):
    date = models.DateField(auto_now_add=True)
    mobileNo = models.IntegerField(
        max_length=10, validators=[mobileNoValidate])
    aadharNo = models.IntegerField(max_length=12)
    name = models.CharField(max_length=100)
    serviceSelected = models.CharField(max_length=255)
    requiredDocuments = models.BooleanField(default=False)
    status = models.BooleanField(default=False)


class VolunteerRating(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    volunteer = models.CharField(max_length=120)
    rating = models.IntegerField()
