# Generated by Django 4.1.5 on 2023-04-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ransom', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
