# Generated by Django 4.1.5 on 2023-04-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ransom', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
