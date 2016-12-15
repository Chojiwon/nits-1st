import re
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


'''
def phonenumber_validator(phonenumber):
    if not re.match(r'^01[016789][1-9]\d{6,7}$', phonenumber):
        raise ValidationError('휴대폰번호를 입력해주세요.')
'''

phonenumber_validator = RegexValidator(r'^01[016789][1-9]\d{6,7}$',
        message='휴대폰 번호를 입력해주세요.')

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, validators=[phonenumber_validator])
    address = models.CharField(max_length=100)

