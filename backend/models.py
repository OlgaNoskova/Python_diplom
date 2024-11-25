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


class User(AbstractUser):
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']





