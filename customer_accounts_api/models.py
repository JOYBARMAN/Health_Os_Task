from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None, password2=None):
        """
        Creates and saves a User with the given email,name,tc and password.
        """
        if not email:
            raise ValueError('Customer must have an email address')
        if not phone:
            raise ValueError('Customer must have an phone number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None):
        """
        Creates and saves a superuser with the given phone,email,name and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            phone=phone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# create a custom user model name customer that contain a unique phone number

class Customer(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
    )
    name = models.CharField(max_length=200)
    phone = PhoneNumberField(verbose_name="Phone",unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name','email']

    def __str__(self):
        return str(self.phone) +" "+str(self.name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

