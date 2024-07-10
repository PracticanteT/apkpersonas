# Generated by Django 5.0.6 on 2024-05-31 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_alter_informacionempleado_fecha_de_retiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionempleado',
            name='motivo_de_retiro',
            field=models.CharField(blank=True, choices=[('renuncia voluntaria', 'Renuncia Voluntaria'), ('terminacion de contrato', 'Terminación de Contrato')], max_length=30, null=True),
        ),
    ]
