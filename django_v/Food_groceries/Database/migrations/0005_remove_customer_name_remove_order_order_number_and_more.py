# Generated by Django 4.2.7 on 2023-12-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
