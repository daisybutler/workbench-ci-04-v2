# Generated by Django 3.2.3 on 2021-07-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_stripe_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='qty',
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(default='location', max_length=25),
            preserve_default=False,
        ),
    ]
