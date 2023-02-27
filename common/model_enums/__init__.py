"""
This module consists of generic model enums
"""
from django.db import models
from django.utils.translation import gettext_lazy as _



class Gender(models.TextChoices):
    """ Choices for customer gender """
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHERS = "O", _("Others")
