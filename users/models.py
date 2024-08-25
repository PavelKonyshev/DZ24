from django.contrib.auth.models import AbstractUser
from django.db import models
from django_celery_beat.utils import now
from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    cyti = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    last_login = models.DateTimeField(default=now, verbose_name="Время последнего посещения")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payment(models.Model):
    PAYMENT_CASH = "cash"
    PAYMENT_TRANSFER = "transfer"
    PAYMENT_CHOICES = (
        (PAYMENT_CASH, "Оплата наличными"),
        (PAYMENT_TRANSFER, "Безналичная оплата"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    date_payment = models.DateTimeField(verbose_name="дата оплаты", auto_now_add=True)
    lesson_paid = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="оплаченный урок", **NULLABLE
    )
    course_paid = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLABLE
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="сумма оплаты"
    )
    payment_type = models.CharField(
        max_length=50, choices=PAYMENT_CHOICES, verbose_name="тип оплаты"
    )
    session_id = models.CharField(max_length=255, verbose_name='id сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)
    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"

    def __str__(self):
        return f'{self.user.email} - {self.lesson_paid.title if self.lesson_paid else self.course_paid.title}'