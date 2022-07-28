# Generated by Django 4.0.6 on 2022-07-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_userdata_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='choise',
            field=models.CharField(blank=True, choices=[('public', 'public'), ('private', 'private')], default='public', max_length=20),
        ),
        migrations.AddField(
            model_name='userdata',
            name='imagename',
            field=models.CharField(blank='image/', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='blogtext',
            field=models.TextField(default='', max_length=1000),
        ),
    ]