# Generated by Django 4.0.2 on 2022-02-08 15:52

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='student_pics')),
                ('passport', models.CharField(max_length=15)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Covid_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=12)),
                ('result', models.CharField(max_length=8)),
                ('date_time', models.DateTimeField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_test', to='corona.profile')),
            ],
        ),
    ]
