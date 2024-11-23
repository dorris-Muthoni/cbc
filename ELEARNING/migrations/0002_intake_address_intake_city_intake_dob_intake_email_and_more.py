# Generated by Django 5.1.3 on 2024-11-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ELEARNING', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='address',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='city',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='dob',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='email',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='fname',
            field=models.CharField(default='Unknown', max_length=20, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='intake',
            name='lname',
            field=models.CharField(default='Unknown', max_length=20, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='intake',
            name='mname',
            field=models.CharField(default='Unknown', max_length=20, verbose_name='Middle Name'),
        ),
        migrations.AddField(
            model_name='intake',
            name='phone_number',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='state',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='zip_code',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=20, null=True),
        ),
    ]