# Generated by Django 4.2.3 on 2023-08-19 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_profile_mobile_remove_profile_otp_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
