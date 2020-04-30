from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UserProfileManager(BaseUserManager):

    # id = models.IntegerField(primary_key=True,unique=True)

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an Email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # id = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
