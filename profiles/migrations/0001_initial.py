# Generated by Django 3.2.3 on 2021-07-05 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_first_name', models.CharField(max_length=25)),
                ('default_last_name', models.CharField(max_length=25)),
                ('default_email', models.EmailField(max_length=254)),
                ('default_password', models.CharField(max_length=25)),
                ('default_phone_number', models.CharField(max_length=20)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_billing_address', models.CharField(max_length=80)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
