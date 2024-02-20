# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.
# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=128)
#     age = models.IntegerField(default=18)
#     gender = models.BooleanField(default=True)
#     grade = models.IntegerField(default=1)
#     major = models.CharField(max_length=25)
#     status = models.BooleanField(default=True)
#     additional_info = models.TextField(default='Test')
#     reservation = models.CharField(max_length=3, default='123')
#     profile_pic = models.ImageField(upload_to='media/profile_pics', default='media/profile_pics/default.jpg')
#     isStudent = models.BooleanField(default=True)


class AuthUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('Username'), unique=True, max_length=50)
    email = models.EmailField(_('Email address'), unique=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True, blank=True)
    is_staff = models.BooleanField(_('is_staff'), default=False, blank=True)
    age = models.IntegerField(default=18, blank=True)
    gender = models.BooleanField(default=True, )
    grade = models.IntegerField(default=1,blank=True)
    major = models.CharField(max_length=25, default='is',blank=True)
    status = models.BooleanField(default=True)
    additional_info = models.TextField(default='Test')
    reservation = models.CharField(max_length=3, default='123')
    profile_pic = models.ImageField(upload_to='media/profile_pics', default='media/profile_pics/default.jpg')
    isStudent = models.BooleanField(default=True)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


class AboutPiece(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.FileField(upload_to=f'media/about')

    def __str__(self):
        return str(self.id)

