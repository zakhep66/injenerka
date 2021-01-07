# Generated by Django 3.1.2 on 2021-01-07 16:42

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20210106_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True, verbose_name='Дата')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.cart', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('description', models.TextField(null=True, verbose_name='Описание продукта')),
                ('category', models.CharField(max_length=50, verbose_name='Категория продукта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена продукта')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.CreateModel(
            name='TableOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.customer', verbose_name='Клиент')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.TextField(verbose_name='Коментарий')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.customer', verbose_name='Клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('Avatar', models.ImageField(upload_to=None, verbose_name='Аватарка')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Logins',
            },
        ),
        migrations.CreateModel(
            name='ImgProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(unique=True, verbose_name='Ссылка на картинку')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'ImgProduct',
                'verbose_name_plural': 'ImgProducts',
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.cart', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.product', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.customer', verbose_name='Покупатель'),
        ),
    ]