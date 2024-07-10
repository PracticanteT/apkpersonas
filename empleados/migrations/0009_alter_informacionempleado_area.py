# Generated by Django 5.0.6 on 2024-06-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_alter_informacionempleado_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionempleado',
            name='area',
            field=models.CharField(choices=[('0', 'Prointimo'), ('2', 'Dirección Comercial'), ('3', 'Dirección Mercado y Diseño'), ('4', 'Técnica'), ('5', 'Dirección de Logística'), ('6', 'Materias Primas'), ('7', 'Laboratorio de Muestras'), ('8', 'Planta de Confección'), ('9', 'Corte'), ('10', 'Producto Terminado'), ('11', 'Calidad Producción'), ('12', 'Ingeniería'), ('13', 'Gestión de Talento Humano'), ('14', 'Sistemas'), ('15', 'Financiera'), ('17', 'Costos'), ('19', 'Comercio Exterior'), ('20', 'Coordinación Zona Franca'), ('23', 'Estudiantes en Práctica'), ('26', 'Preproducción Ropa Interior'), ('27', 'Auditoría'), ('28', 'Gerencia de Abastecimientos')], max_length=50),
        ),
    ]
