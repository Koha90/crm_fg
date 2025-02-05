# Generated by Django 3.1.5 on 2021-02-06 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30, verbose_name='Должность')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=30, null=True, unique=True, verbose_name='Ссылка на профиль')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ('user',),
            },
        ),
    ]
