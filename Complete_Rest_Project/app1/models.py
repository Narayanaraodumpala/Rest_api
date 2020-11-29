
from django.db import models


# Create your models here.



class TyreModel(models.Model):
    tyre_number=models.PositiveIntegerField()

    tyre_company=models.CharField(max_length=30)
    tyre_brand=models.CharField(max_length=20)
    tyre_cost=models.FloatField()
    lifetime=models.CharField(max_length=20)

    def __str__(self):
        return self.tyre_company

class Carplan(models.Model):

    plan_id=models.IntegerField()
    plan_name=models.CharField(max_length=30)
    current_status=models.CharField(max_length=30)
    plan_validity=models.PositiveIntegerField()

    def __str__(self):
        return self.plan_name


class CarspaceModel(models.Model):
    car_number=models.IntegerField(null=True)
    car_tyres=models.ForeignKey(TyreModel,on_delete=models.CASCADE,null=True,default=None)
    car_plan=models.ForeignKey(Carplan,on_delete=models.CASCADE,null=True,default=None)
    car_name=models.CharField(max_length=30,null=True)
    car_brand=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=100,null=True)
    production=models.IntegerField(null=True)
    fuel =models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.car_name



    objects = models.Manager()

from django.utils import timezone
now=timezone.now()
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff,
                     is_acive, is_superuser, **extra_fields):

        if not username:
            raise ValueError("The  given Username is not valid")
        email=self.normalize_email(email)
        user=self.model(username=username,email=email,is_acive=False,
                        is_staff=is_staff,is_superuser=is_superuser,
                        timezone=now,**extra_fields)
        user.set_password(password)
        user.save(self.db)
        return user

    def create_user(self,username,email,password,**extra_fields):
        return self._create_user(username,email,password,is_acive=True,is_staff=False,is_superuser=False,**extra_fields)


    def create_superuser(self,username,email,password, **extra_fields):
        user=self._create_user(username,email,password,is_acive=True,is_staff=True,is_superuser=True,**extra_fields)
        user.save(using=self.db)
        return user



class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=200,unique=True)
    email=models.EmailField(max_length=300,unique=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now())
    receive_newsletter=models.BooleanField(default=False)
    birth_date=models.DateTimeField(null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    about_me=models.TextField(max_length=500,blank=True,null=True)
    profile_image=models.ImageField(upload_to='images/',null=True)

    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email',]









