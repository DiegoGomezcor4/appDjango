# Generated by Django 5.2.1 on 2025-05-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_producto_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(blank=True, to='inventario.proveedor'),
        ),
    ]
