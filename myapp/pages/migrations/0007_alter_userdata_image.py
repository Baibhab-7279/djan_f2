# Generated by Django 4.0.6 on 2022-07-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]