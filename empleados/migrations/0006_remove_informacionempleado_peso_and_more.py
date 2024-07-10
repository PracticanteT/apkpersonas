# Generated by Django 5.0.6 on 2024-05-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_alter_informacionempleado_motivo_de_retiro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacionempleado',
            name='peso',
        ),
        migrations.AlterField(
            model_name='informacionempleado',
            name='estado_civil',
            field=models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('union libre', 'Union Libre'), ('viudo/a', 'Viudo/a')], max_length=12),
        ),
    ]
