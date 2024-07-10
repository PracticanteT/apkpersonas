# Generated by Django 5.0.6 on 2024-06-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0014_alter_informacionempleado_centro_de_costos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosrealizados',
            name='Area',
            field=models.CharField(blank=True, choices=[('artes y diseño', 'Artes y Diseño'), ('ciencias ambientales', 'Ciencias Ambientales'), ('ciencias de la salud', 'Ciencias de la Salud'), ('ciencias naturales y exactas', 'Ciencias Naturales y Exactas'), ('ciencias sociales', 'Ciencias Sociales'), ('comercio exterior', 'Comercio Exterior'), ('Comunicacion y periodismo', 'Comunicacion y Periodismo'), ('bachiller academico', 'Bachiller Academico'), ('diseño de modas', 'Diseño de Modas'), ('educacion', 'Educacion'), ('humanidades', 'Humanidades'), ('ingenieria y tecnologia', 'Ingenieria y Tecnologia'), ('mercadotecnia de moda', 'Mercado Tecnica de Moda'), ('negocios y administracion', 'Negocios y Administracion'), ('nutricion y dietetica', 'Nutricion y Dietetica'), ('textil', 'textil'), ('veterinaria', 'veterinaria')], max_length=50, null=True),
        ),
    ]
