from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, Group, GroupManager
from .validators import validate_username
from django.utils.timezone import now


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email must be provided')
        user = self.model(
        email = self.normalize_email(email),
        )  
        user.set_password(password)
        user.save(using= self._db)
        return user


    def create_staffuser(self, email, password):
        user = self.create_user(
            email =email,
            password = password.password,

        )
        user.is_staff = True
        user.save(using = self._db  )
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email = email,
            password = password,
           
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email =         models.EmailField(max_length=255, unique=True, verbose_name='Email')
    first_name =    models.CharField(max_length=100, verbose_name='First Name')
    last_name =     models.CharField(max_length=100, verbose_name='Last Name')
    is_manager =    models.BooleanField(default=False, verbose_name='Manager')
    is_teacher =    models.BooleanField(default=False,verbose_name= 'Teacher')
    is_student =    models.BooleanField(default=False, verbose_name='Student')
    is_suspended =  models.BooleanField(default=False, verbose_name='Suspended')
    is_active =     models.BooleanField(default=True, verbose_name='Active')
    is_staff =      models.BooleanField(default=False, verbose_name='Staff')
    is_admin =      models.BooleanField(default=False, verbose_name='Admin')
    date_joined =   models.DateTimeField(verbose_name='Date Joined',auto_now_add= True)
    last_login =    models.DateTimeField(verbose_name='Last Active', auto_now=True)
    group = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='user_set', related_query_name='user')
        
    class Meta:
        db_table = 'Account'

    def __str__(self):
        return self.email
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True