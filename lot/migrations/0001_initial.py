# Generated by Django 4.1.5 on 2023-01-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('idLot', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('del_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
