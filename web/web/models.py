from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  AbstractBaseUser, UserManager, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, id, name, password=None):
        if not id:
            raise ValueError('must have user id')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            name=name,
            id=self.normalize_email(id),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, id, name, password=None):
        user = self.create_user(
            name=name,
            id=self.normalize_email(id),
            password=password
        )
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=500)
    name = models.CharField(max_length=500)
    password  = models.CharField(max_length=1000, db_column='pw')
    reg_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff= models.BooleanField(default=False, verbose_name="관리자")
    is_active= models.BooleanField(default=True, verbose_name="사용여부")

    USERNAME_FIELD = 'id'
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = "계정"
        verbose_name_plural = "계정"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True