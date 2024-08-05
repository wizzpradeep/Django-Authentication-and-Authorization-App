from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, User

# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fileds):
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError("Superuser must  have is_staff True.")
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser True.")
        return self.create_user(email,password,**extra_fileds)
        

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,blank=True)
    username = models.CharField(unique=True, blank=True, max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

    def __str__(self):
        return self.username
    


class EmailVerification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=None) 