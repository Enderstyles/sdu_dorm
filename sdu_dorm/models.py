# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.


def news_image_upload(instance, filename):
    return 'news/{0}/{1}'.format(instance.id, filename)


class NewsCategories(models.Model):
    category_name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.category_name


class NewsPost(models.Model):
    news_title = models.TextField(default="News title")
    news_description = models.TextField(default="News description")
    main_image = models.ImageField(upload_to=news_image_upload)
    what_to_expect = models.TextField(blank=True)
    registration = models.TextField(default="Registration", blank=True)
    additional_info = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_of_the_event = models.DateField(blank=True)
    time_of_the_event = models.TimeField(blank=True)
    place_of_the_event = models.TextField(blank=True)
    category_of_the_event = models.ForeignKey(NewsCategories, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.news_title)


class AuthUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, student_id, password, **extra_fields):
        """
        Creates and saves a User with the given student_id and password.
        """
        if not student_id:
            raise ValueError('The given email must be set')
        student_id = self.normalize_email(student_id)
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(student_id, password, **extra_fields)

    def create_superuser(self, student_id, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(student_id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(_('student_id'), unique=True, max_length=10)
    email = models.EmailField(_('Email address'), blank=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True, blank=True)
    is_staff = models.BooleanField(_('is_staff'), default=False, blank=True)
    age = models.IntegerField(default=18, blank=True)
    gender = models.IntegerField(default=True)
    grade = models.FloatField(default=1, blank=True)
    major = models.CharField(max_length=25, default='is', blank=True)
    status = models.BooleanField(default=True)
    reservation = models.CharField(max_length=4, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    isStudent = models.BooleanField(default=True)
    follows = models.ManyToManyField(NewsPost, through="Enrollment")

    objects = AuthUserManager()

    USERNAME_FIELD = 'student_id'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.student_id


class Enrollment(models.Model):
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class AboutPost(models.Model):
    type = models.CharField(max_length=30, blank=True)
    description = models.TextField(default="The description")
    name_of_head_of_dormitory = models.CharField(max_length=30, blank=False, default="Name")
    contacts_head_of_dormitory = models.TextField(default="email@mail.com +77079999999", blank=True)
    contacts_reception = models.TextField(default="+77017777777", blank=True)
    contacts_medical_care = models.TextField(default="+77050010101", blank=True)
    contacts_security_service = models.TextField(default="+77778881122", blank=True)

    main_image1 = models.ImageField(upload_to=f'about/main', blank=True)
    main_image2 = models.ImageField(upload_to=f'about/main', blank=True)
    main_image3 = models.ImageField(upload_to=f'about/main', blank=True)
    main_image4 = models.ImageField(upload_to=f'about/main', blank=True)
    main_image5 = models.ImageField(upload_to=f'about/main', blank=True)

    social_life_description = models.TextField(default="Social life description", blank=True)
    social_life_image1 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image2 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image3 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image4 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image5 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image6 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image7 = models.ImageField(upload_to=f'about/social_life', blank=True)
    social_life_image8 = models.ImageField(upload_to=f'about/social_life', blank=True)

    safety_members = models.TextField(default="70 members")
    safety_description = models.TextField(default="safety description", blank=True)
    working_hours = models.TextField(default="Working hours", blank=True)
    working_hours_description = models.TextField(default="are from 6:00 to 22:00", blank=True)

    def __str__(self):
        return str(self.type)


class MainPageModel(models.Model):
    main_banner_img = models.ImageField(upload_to='main_page', default='profile_pics/default.jpg')

    main_title = models.TextField(default="Mail title")
    main_description = models.TextField(default="some text for test")
    mission_title = models.TextField(default="Mission title")
    mission_description = models.TextField(default="Mission description")
    responsibilities_title = models.TextField(default="Responsibilities title")
    responsibilities_description = models.TextField(default="Responsibilities description")

    deadlines_title = models.TextField(default="Deadlines title")
    deadlines_description = models.TextField(default="Deadlines")
    docs_required_title = models.TextField(default="Docs title")
    decs_required_description = models.TextField(default="Decs description")

    dorm_image1 = models.ImageField(upload_to='main_page/dorm_images', blank=True)
    dorm_image2 = models.ImageField(upload_to='main_page/dorm_images', blank=True)
    dorm_image3 = models.ImageField(upload_to='main_page/dorm_images', blank=True)
    dorm_image4 = models.ImageField(upload_to='main_page/dorm_images', blank=True)
    dorm_image5 = models.ImageField(upload_to='main_page/dorm_images', blank=True)
