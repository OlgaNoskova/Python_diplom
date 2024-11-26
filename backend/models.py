from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.validators import validate_quantity


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название магазина')
    url = models.CharField(max_length=255, verbose_name='URL адрес магазина', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины', related_name='categories')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductInitial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    product = models.ForeignKey(ProductInitial, on_delete=models.CASCADE, verbose_name='Продукт', related_name='product')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин', related_name='product')
    quantity = models.IntegerField(validators=[validate_quantity], default=0, verbose_name='Количество в магазине')
    price = models.IntegerField(verbose_name='Цена')
    price_rrc = models.IntegerField(verbose_name='Рекомендуемая розничная цена')

    class Meta:
        verbose_name = 'Продукт в магазине'
        verbose_name_plural = 'Продукты в магазине'
        ordering = ['name']

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=255, verbose_name='Параметр продукта')

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='parameters')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, verbose_name='Параметр продукта',
                                  related_name='parameters')
    description = models.CharField(max_length=255, verbose_name='Описание продукта')

    class Meta:
        verbose_name = 'Параметр продукта'
        verbose_name_plural = 'Параметры продуктов'


class CustomUserManager(BaseUserManager):               # Переопределение менеджера пользователя
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле электронной почты должно быть заполнено")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        print("Creating superuser...")
        print(f"Email: {email}, Password: {password}, Extra Fields: {extra_fields}")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Суперпользователь должен иметь is_superuser=True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Электронная почта', blank=False, unique=True)
    password = models.CharField(max_length=100, verbose_name='Пароль')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')
    building = models.CharField(max_length=100, verbose_name='Строение')
    structure = models.CharField(max_length=100, verbose_name='Корпус')
    flat = models.CharField(max_length=100, verbose_name='Квартира')
    is_admin = models.BooleanField(default=False)

    # Указываем, что менеджером для данной модели будет CustomUserManager
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']





