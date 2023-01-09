import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from tasks.models import Task

"""
Modificate default User Manager and User Model
"""


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        role,
        password,
        controll_question=None,
        answer_controll_question=None,
        nickname=None,
        commit=True,
    ):

        if not email:
            raise ValueError(_("Users must have an email address"))
        if not password:
            raise ValueError(_("Users must set a strong password"))
        if not role:
            raise ValueError(_("Users must choose the role "))

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            controll_question=controll_question,
            answer_controll_question=answer_controll_question,
            nickname=nickname,
        )

        user.set_password(password)
        user.full_clean()

        if commit:
            user.save(using=self._db)

        return user

    def create_superuser(self, email, password, role):

        user = self.create_user(
            email,
            password=password,
            role=role,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


ROLE_CHOICES = (
    ("STUDENT", "Student"),
    ("TEACHER", "Teacher"),
    ("ADMIN", "Admin"),
)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=150, unique=True, verbose_name=_("email address"))
    nickname = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="STUDENT")
    account_image = models.ImageField(upload_to="account/%Y/%m/%d/", blank=True)
    controll_question = models.CharField(
        max_length=250, verbose_name=_("controll question"), blank=True, null=True
    )
    answer_controll_question = models.CharField(
        max_length=150, verbose_name=_("answer to controll question"), blank=True, null=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Defines whether the user should be set as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Defines whether the user can log into this admin site."),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["role"]

    def get_absolute_url(self):
        return reverse(viewname="view_account", kwargs={"pk": self.id})  # type:ignore

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class Student(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    current_task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True)


class Teacher(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    short_bio = models.CharField(max_length=250, blank=True)
