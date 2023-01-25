# Generated by Django 4.1.5 on 2023-01-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCategory', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('del_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]