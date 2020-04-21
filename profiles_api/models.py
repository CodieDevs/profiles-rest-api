from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """ Manager for User Profiles"""

    def create_user(self, email, name, password=None):
        """Create a new User Profile"""

        # checking for email provided or not
        if not email:
            raise ValueError('User must have an email address?')

        email = self.normalize_email(email) #half email case-sensitive half case-insensitive

        userModel = self.model(email=email, name=name)
        userModel.set_password(password) # password is encrypted
        userModel.save(using=self._db) #best practice to add this line

        return userModel

         #create super user
    def create_superuser(self, email, name, password):
        """Create & save a new superuser with given details"""

        userModel = self.create_user(email, name, password)

        userModel.is_superuser = True
        userModel.is_staff = True
        userModel.save(using=self._db)

        return userModel


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for UserProfile in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

      # Custom Model Manager
    userProfileManager = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name


    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name


    def __str__(self):
        """Return String Representation of User"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile Status Update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return the Model as a string"""
        return self.status_text
