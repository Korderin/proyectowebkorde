# Generated by Django 5.0.6 on 2024-06-18 02:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pedidos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lineapedido",
            old_name="pedido_id",
            new_name="pedido",
        ),
        migrations.RenameField(
            model_name="lineapedido",
            old_name="producto_id",
            new_name="producto",
        ),
    ]
