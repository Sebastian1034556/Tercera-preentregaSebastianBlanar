# Generated by Django 5.0.2 on 2024-04-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0011_alter_pedido_fecha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="dni",
            field=models.IntegerField(unique=True),
        ),
    ]
