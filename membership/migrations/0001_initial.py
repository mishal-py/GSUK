# Generated by Django 5.2.1 on 2025-05-28 04:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address_uk', models.TextField()),
                ('address_nepal', models.TextField(blank=True)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('membership_type', models.CharField(choices=[('Life', 'Life Membership (£100)'), ('Ordinary', 'Ordinary Membership (£12 for 2 years)')], max_length=20)),
                ('opt_out_contact', models.BooleanField(default=False)),
                ('rules_confirmed', models.BooleanField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
