# Generated by Django 4.0.6 on 2022-07-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_userdata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
