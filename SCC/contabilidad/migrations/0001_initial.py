# Generated by Django 5.0.4 on 2025-03-23 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsientoContable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CuentaContable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('activo', 'Activo'), ('pasivo', 'Pasivo'), ('patrimonio', 'Patrimonio'), ('ingreso', 'Ingreso'), ('gasto', 'Gasto')], max_length=50)),
                ('nivel', models.IntegerField()),
                ('cuenta_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contabilidad.cuentacontable')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAsiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debe', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('haber', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='contabilidad.asientocontable')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.cuentacontable')),
            ],
        ),
    ]
