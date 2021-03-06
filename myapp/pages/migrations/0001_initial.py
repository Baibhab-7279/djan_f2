# Generated by Django 4.0.6 on 2022-08-02 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(default='type your message', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, default='this is by-default')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=10)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10)),
                ('profileimage', models.ImageField(blank=True, upload_to='profileimage')),
                ('profileimagename', models.CharField(blank=True, default='profileimage/', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='post it', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Baibhab@7279', max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('blogtext', models.TextField(default='', max_length=1000)),
                ('uploadtime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('choise', models.CharField(blank=True, choices=[('public', 'public'), ('private', 'private')], default='public', max_length=20)),
                ('imagename', models.CharField(blank=True, default='images/', max_length=100)),
            ],
        ),
    ]
