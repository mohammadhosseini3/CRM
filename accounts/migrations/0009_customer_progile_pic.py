# Generated by Django 4.1 on 2022-09-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='progile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
