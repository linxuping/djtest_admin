from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractUser
from django.db import models

class NewUser(AbstractUser):
    new_field = models.CharField(max_length=100)
    
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class MemberCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            # Not sure why UserCreationForm doesn't do this in the first place,
            # or at least test to see if _meta.model is there and if not use User...
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta:
        model = NewUser
        fields = ("username",)

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = NewUser

class MemberAdmin(UserAdmin):
    form = MemberChangeForm
    add_form = MemberCreationForm

admin.site.register(NewUser, MemberAdmin)
