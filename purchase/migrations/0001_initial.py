# Generated by Django 4.1.5 on 2023-01-26 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lot', '0001_initial'),
        ('user', '0001_initial'),
        ('supplier', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('idPurchase', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('cost', models.FloatField()),
                ('note', models.CharField(max_length=50)),
                ('del_date', models.DateField(auto_now_add=True, null=True)),
                ('idLot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lot.lot')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('idSupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]