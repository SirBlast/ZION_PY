# Generated by Django 4.1.5 on 2023-02-04 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('idLocation', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('settings_admin', models.TextField()),
                ('settings_user', models.TextField()),
                ('phone_contact', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(max_length=50)),
                ('email_contact', models.EmailField(max_length=254)),
                ('del_date', models.DateField(auto_now=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('user_create', models.CharField(max_length=50)),
                ('user_update', models.CharField(max_length=50)),
                ('idCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
