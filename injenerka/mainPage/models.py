from django.db import models
from decimal import *



# Create your models here.

class Customer(models.Model):

    serName = models.CharField(max_length=30, verbose_name='Фамилия клиента')
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    fathName = models.CharField(max_length=30, verbose_name='Отчество клиента')
    tel = models.IntegerField(verbose_name='Номер телефона')
    email = models.EmailField(max_length=40, verbose_name='Email')

    class Meta:

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.serName
    

class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True)
    category = models.CharField(max_length=50, verbose_name='Категория продукта')
    price = models.DecimalField(max_digits=9, verbose_name='Цена продукта', decimal_places=2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Cart(models.Model):

    customer = models.ForeignKey(Customer, verbose_name=("Покупатель"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class CartProduct(models.Model):

    cart = models.ForeignKey("Cart", verbose_name=("Корзина"), on_delete=models.CASCADE)
    product = models.ForeignKey("Product", verbose_name=("Продукт"), on_delete=models.CASCADE)

    def __str__(self):
        return 'Продукт: {} (для корзины)'.format(self.product.title)


class Order(models.Model):

    cart = models.ForeignKey("Cart", verbose_name=("Корзина"), on_delete=models.CASCADE)
    data = models.DateField(("Дата"), auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.data
    


class ProductOrder(models.Model):

    product = models.ForeignKey("Product", verbose_name=("Продукт"), on_delete=models.CASCADE)
    order = models.ForeignKey("Order", verbose_name=("Заказ"), on_delete=models.CASCADE)

    def __str__(self):
        return 'Продукт для заказа'.format(self.product.title)


class ImgProduct(models.Model):
    product = models.ForeignKey("Product", verbose_name=("Продукт"), on_delete=models.CASCADE)
    url = models.SlugField(("Ссылка на картинку"), max_length=50, unique=True)

    class Meta:
        verbose_name = 'ImgProduct'
        verbose_name_plural = 'ImgProducts'

    def __str__(self):
        return 'Картинка для продукта'.format(self.product.title)


class Login(models.Model):
    login = models.CharField(("Login"), max_length=50)
    password = models.CharField(("Password"), max_length=50)
    Avatar = models.ImageField(("Аватарка"), upload_to=None, height_field=None, width_field=None, max_length=None)
    customer = models.ForeignKey("Customer", verbose_name=("Клиент"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'

    def __str__(self):
        return self.login


class TableOrders(models.Model):
    customer = models.ForeignKey("Customer", verbose_name=("Клиент"), on_delete=models.CASCADE)

    def __str__(self):
        return 'Таблица заказов'.format(self.customer.name)


class Rating(models.Model):
    product = models.ForeignKey("Product", verbose_name=("Продукт"), on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", verbose_name=("Клиент"), on_delete=models.CASCADE)
    rating = models.TextField(("Коментарий"))

    def __str__(self):
        return 'Коментарий клиента'.format(self.product.title)
    