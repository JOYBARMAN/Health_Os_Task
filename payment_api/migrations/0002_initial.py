# Generated by Django 4.1.5 on 2023-01-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_api', '0001_initial'),
        ('subscription_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription_api.subscription'),
        ),
    ]
