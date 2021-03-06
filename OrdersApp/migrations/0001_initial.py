# Generated by Django 3.1.6 on 2021-02-05 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('financialAccount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('itemCode', models.IntegerField()),
                ('price', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('publishedAt', models.DateTimeField(auto_now=True)),
                ('deadLine', models.DateTimeField()),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrdersApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RecordInOrder',
            fields=[
                ('recordId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrdersApp.item')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrdersApp.order')),
            ],
        ),
    ]
