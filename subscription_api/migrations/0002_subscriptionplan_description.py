# Generated by Django 4.1.5 on 2023-01-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]
