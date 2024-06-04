from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

role = (
    ('admin', 'Administrator'),
    ('staff', 'Staff'),
    ('user', 'User')
)

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    username = CICharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = CIEmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    number = models.CharField(max_length=10)
    dob = models.DateField(help_text=_("In B.S"))

    role = models.CharField(max_length=20, choices=role)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    LOGIN_FIELD = "username"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")