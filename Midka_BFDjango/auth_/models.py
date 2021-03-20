from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from utils.constants import USER_ROLES, USER_ROLE_GUEST
# Create your models here.





class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fiels):
        if not username:
            raise ValueError('set username')
        user = self.model(username= username, **extra_fiels)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password = None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fiels)

    def create_superuser(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        extra_fiels.setdefault('is_stuff', True)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)

class MainUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',max_length=30, unique=True)
    first_name = models.CharField(('first_name'),max_length=30, blank=True)
    last_name = models.CharField(('last_name'),max_length=30, blank=True)
    email = models.EmailField(('email'),max_length=30, blank=True)
    data_joined = models.DateTimeField('data_joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_ROLE_GUEST)
    # profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT, related_name='profile', verbose_name='Profile', default=False)
    objects = MainUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class UserProfile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, default=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

