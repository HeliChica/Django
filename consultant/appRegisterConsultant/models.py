from django.db import models


# Create your models here.

class Persons(models.Model):
    ID = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
    name = models.CharField(
        name=None,
        max_length=200,
        blank=False,
        null=False
    )
    surname = models.CharField(
        name=None,
        max_length=200,
        blank=False,
        null=False
    )
    birthDate = models.DateField(
        name=None,
        null=False,
        blank=False
    )

    SEX_STATUS = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    )

    sex = models.CharField(
        name=None,
        max_length=1,
        choices=SEX_STATUS,
        blank=False,
        null=False,
        default='m',
        help_text='Sexo de la persona'
    )
    category = models.CharField(
        name=None,
        max_length=100,
        blank=False,
        null=False
    )
    recordDate = models.DateField(
        name=None,
        blank=False,
        null=False
    )


class Studies(models.Model):
    ID = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
    graduationDate = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
    degree = models.CharField(
        name=None,
        max_length=200,
        blank=False,
        null=False
    )
    establishment = models.CharField(
        name=None,
        max_length=200,
        blank=False,
        null=False
    )


class Jobs(models.Model):
    ID = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
    startDate = models.CharField(
        name=None,
        max_length=7,
        blank=False,
        null=False
    )
    endDate = models.CharField(
        name=None,
        max_length=7,
        blank=False,
        null=False
    )
    company = models.CharField(
        name=None,
        max_length=200,
        blank=False,
        null=False
    )
    duties = models.TextField(
        name=None,
        blank=True,
        null=True
    )


class Products(models.Model):
    ID = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
    serviceCode = models.IntegerField(
        name=None,
        blank=False,
        null=False
    )
