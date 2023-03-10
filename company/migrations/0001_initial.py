# Generated by Django 4.1.5 on 2023-02-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('idCompany', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_contact', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('settings_admin', models.TextField()),
                ('settings_user', models.TextField()),
                ('phone_contact', models.CharField(max_length=50)),
                ('cell_phone_contact', models.CharField(max_length=50)),
                ('email_contact', models.EmailField(max_length=254)),
                ('del_date', models.DateField(auto_now=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('user_create', models.CharField(max_length=50)),
                ('user_update', models.CharField(max_length=50)),
            ],
        ),
    ]
