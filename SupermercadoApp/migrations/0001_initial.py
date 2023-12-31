# Generated by Django 4.2.5 on 2023-10-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('domicilio', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=30)),
                ('apellido_empleado', models.CharField(max_length=30)),
                ('puesto', models.CharField(max_length=20)),
                ('sueldo', models.IntegerField()),
                ('numero_identidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('tamanio', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rut', models.IntegerField()),
                ('categoria_producto', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=40)),
            ],
        ),
    ]
