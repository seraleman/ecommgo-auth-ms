# Generated by Django 3.2.7 on 2021-11-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authMsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='document',
            field=models.CharField(default=100000000, max_length=20, verbose_name='Document'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='Manrique', max_length=30, verbose_name='LastName'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='3003030000', max_length=20, verbose_name='PhoneNumber'),
            preserve_default=False,
        ),
    ]