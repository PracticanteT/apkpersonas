# Importa ValidationError desde django.core.exceptions para manejo de errores de validación.
from django.core.exceptions import ValidationError
# Importa models desde django.db para definir modelos.
from django.db import models
# Importa date desde datetime para calcular la edad segun la fecha de nacimiento
from datetime import date

# Define la clase informacionempleado que hereda de models.Model.
class informacionempleado(models.Model):
    # Campo de carácter con longitud máxima de 10, utilizado como clave primaria.
    codigo_empleado = models.CharField(max_length=10, primary_key=True)
    
    # Campo de carácter con longitud máxima de 10, con opciones limitadas.
    estado = models.CharField(max_length=10, choices=[
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo')
    ])
    
    # Campos de carácter con longitudes máximas específicas.
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    
    # Campo de carácter con opciones para el género.
    genero = models.CharField(max_length=10, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ])
    
    # Campo de carácter con opciones para el tipo de sangre.
    tipo_de_sangre = models.CharField(max_length=3, choices=[
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ])
    
    # Campo de fecha para la fecha de nacimiento.
    fecha_de_nacimiento = models.DateField()
    # Campo de carácter con longitud máxima de 50.
    lugar_de_nacimiento = models.CharField(max_length=50)
    
    # Campo de carácter con opciones para la estatura.
    estatura = models.CharField(max_length=6, choices=[
        ('140 cm', '1,40 cm'),
        ('141 cm', '1,41 cm'),
        ('142 cm', '1,42 cm'),
        ('143 cm', '1,43 cm'),
        ('144 cm', '1,44 cm'),
        ('145 cm', '1,45 cm'),
        ('146 cm', '1,46 cm'),
        ('147 cm', '1,47 cm'),
        ('148 cm', '1,48 cm'),
        ('149 cm', '1,49 cm'),
        ('150 cm', '1,50 cm'),
        ('151 cm', '1,51 cm'),
        ('152 cm', '1,52 cm'),
        ('153 cm', '1,53 cm'),
        ('154 cm', '1,54 cm'),
        ('155 cm', '1,55 cm'),
        ('156 cm', '1,56 cm'),
        ('157 cm', '1,57 cm'),
        ('157 cm', '1,58 cm'),
        ('158 cm', '1,58 cm'),
        ('159 cm', '1,59 cm'),
        ('160 cm', '1,60 cm'),
        ('161 cm', '1,61 cm'),
        ('162 cm', '1,62 cm'),
        ('163 cm', '1,63 cm'),
        ('164 cm', '1,64 cm'),
        ('165 cm', '1,65 cm'),
        ('166 cm', '1,66 cm'),
        ('167 cm', '1,67 cm'),
        ('168 cm', '1,68 cm'),
        ('169 cm', '1,69 cm'),
        ('170 cm', '1,70 cm'),
        ('171 cm', '1,71 cm'),
        ('172 cm', '1,72 cm'),
        ('173 cm', '1,73 cm'),
        ('174 cm', '1,74 cm'),
        ('175 cm', '1,75 cm'),
        ('176 cm', '1,76 cm'),
        ('177 cm', '1,77 cm'),
        ('178 cm', '1,78 cm'),
        ('179 cm', '1,79 cm'),
        ('180 cm', '1,80 cm'),
        ('181 cm', '1,81 cm'),
        ('182 cm', '1,82 cm'),
        ('183 cm', '1,83 cm'),
        ('184 cm', '1,84 cm'),
        ('185 cm', '1,85 cm'),
        ('186 cm', '1,86 cm'),
        ('187 cm', '1,87 cm'),
        ('188 cm', '1,88 cm'),
        ('189 cm', '1,89 cm'),
        ('190 cm', '1,90 cm'),
        ('191 cm', '1,91 cm'),
        ('192 cm', '1,92 cm'),
        ('193 cm', '1,93 cm'),
        ('194 cm', '1,94 cm'),
        ('195 cm', '1,95 cm'),
        ('196 cm', '1,96 cm'),
        ('197 cm', '1,97 cm'),
        ('198 cm', '1,98 cm'),
        ('199 cm', '1,99 cm'),
    ])
    
    # Campos de carácter con opciones para la talla de camisa y sudadera.
    talla_camisa = models.CharField(max_length=3, choices=[
        ('M', 'M'),
        ('S', 'S'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ])
    talla_sudadera = models.CharField(max_length=3, choices=[
        ('M', 'M'),
        ('S', 'S'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ])
    
    # Campo de entero con opciones para la talla de calzado.
    talla_calzado = models.IntegerField(choices=[
        (34, '34'),
        (35, '35'),
        (36, '36'),
        (37, '37'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
        (41, '41'),
        (42, '42'),
        (43, '43'),
        (44, '44'),
        (45, '45'),
    ])

    # Campo de carácter con opciones para el estado civil.
    estado_civil = models.CharField(max_length=12, choices=[
        ('Soltero', 'Soltero/a'),
        ('Casado', 'Casado/a'),
        ('Union libre', 'Union Libre'),
        ('Viudo/a', 'Viudo/a'),
    ])
    
    # Campo de carácter con opciones para el tipo de vivienda.
    tipo_de_vivienda = models.CharField(max_length=10, choices=[
        ('Propia', 'Propia'),
        ('Arrendada', 'Arrendada'),
        ('Familiar', 'Familiar'),
    ])

    vehiculo = models.CharField(null=True, blank=True, max_length=20, choices=[
        ('Ninguno', 'Ninguno'),
        ('Motocicleta', 'Motocicleta'),
        ('Automovil', 'Automovil'),
    ])
    
    # Campos de carácter para la dirección, contacto y contacto de emergencia.
    direccion = models.CharField(max_length=50)
    contacto = models.CharField(max_length=10)
    contacto_de_emergencia = models.CharField(max_length=10)
    
    # Campo de carácter para el correo electrónico.
    correo_electronico = models.CharField(max_length=50)
    
    # Campo de carácter para las restricciones médicas.
    restricciones_medicas = models.CharField(max_length=100)
    
    # Campo de carácter con opciones para la ARL.
    arl = models.CharField(max_length=20, choices=[
        ('Axa colpatria', 'Axa Colpatria')
    ])
    
    # Campo de carácter con opciones para el riesgo ARL.
    riesgo_arl = models.CharField(max_length=10, choices=[
        ('1.044', '1.044')
    ])
    
    # Campo de carácter con opciones para la EPS.
    eps = models.CharField(max_length=50, choices=[
        ('Sura eps', 'Sura EPS'),
        ('Sanitas eps', 'Sanitas EPS'),
        ('Nueva empresa promotora de salud', 'Nueva Empresa Promotora de Salud'),
        ('Alianza medellin antioquia eps sas - savia salud', 'Alianza Medellin Antioquia EPS SAS - Savia Salud'),
        ('Salud total eps', 'Salud Total EPS'),
    ])
    
    # Campo de carácter con opciones para el administrador del fondo de pensiones.
    administrador_fondo_de_pensiones = models.CharField(max_length=20, choices=[
        ('Proteccion', 'Protección'),
        ('Colpensiones', 'Colpensiones'),
        ('Porvenir', 'Porvenir'),
        ('Colfondos', 'Colfondos'),
        ('Skandia', 'Skandia'),
    ])
    
    # Campo de carácter con opciones para el fondo de cesantías.
    fondo_de_cesantias = models.CharField(max_length=50, choices=[
        ('Proteccion', 'Protección'),
        ('Colfondos', 'Colfondos'),
        ('Fondo nacional del ahorro', 'Fondo Nacional del Ahorro'),
        ('Porvenir', 'Porvenir'),
    ])
    
    # Campo de carácter con opciones para el tipo de contrato.
    tipo_de_contrato = models.CharField(max_length=20, choices=[
        ('Termino indefinido', 'Término Indefinido'),
        ('Termino fijo', 'Término Fijo'),
        ('Practicas', 'Prácticas'),
    ])
    
    # Campo de carácter con opciones para el centro de costos.
    centro_de_costos = models.CharField(max_length=100, choices=[
        ('I101', 'Direccion I101'),
        ('I130', 'Sistemas I130'),
        ('I140', 'Auditoria I140'),
        ('I202', 'Gestion de Talento Humano I202'),
        ('I223', 'Seguridad I223'),
        ('I231', 'Servicios Generales y Aseo I231'),
        ('I250', 'Estudiantes en Practica I250'),
        ('I330', 'Financiera I330'),
        ('I432', 'Comercio Exterior I432'),
        ('I502', 'Producto Terminado I502'),
        ('I520', 'Comercial I520'),
        ('I760', 'Laboratorio de Muestras I760'),
        ('I770', 'Desarrollo de Producto I770'),
        ('I310', 'Coordinacion de Movimientos I310'),
        ('I360', 'Planeacion I360'),
        ('I431', 'Compras I431'),
        ('I550', 'Gerencia Operativa I550'),
        ('I560', 'Abastecimiento I560'),
        ('I603',' Ingenieria I603'),
        ('I647', 'Planta de Confeccion I647'),
        ('I648', 'Corte I648'),
        ('I560', 'Abastecimiento I560'),
        ('I1603','Ingenieria I1603'),
        ('I647', 'Planta de Confeccion I647'),
        ('I648', 'Corte I648'),
        ('I651', 'Materias Primas I651'),
        ('I663', 'Maquilas I663'),
        ('I651', 'Materias Primas I651'),
        ('I663', 'Maquilas I663'),
        ('I680', 'Calidad Produccion I680'),
       
    ])
    
    # Campo de carácter con opciones para el área.
    area = models.CharField(max_length=50, choices=[
        ('0', 'Prointimo'),
        ('2', 'Dirección Comercial'),
        ('3', 'Dirección Mercado y Diseño'),
        ('4', 'Técnica'),
        ('5', 'Dirección de Logística'),
        ('6', 'Materias Primas'),
        ('7', 'Laboratorio de Muestras'),
        ('8', 'Planta de Confección'),
        ('9',  'Corte'),
        ('10', 'Producto Terminado'),
        ('11', 'Calidad Producción'),
        ('12', 'Ingeniería'),
        ('13', 'Gestión de Talento Humano'),
        ('14', 'Sistemas'),
        ('15', 'Financiera'),
        ('17', 'Costos'),
        ('19', 'Comercio Exterior'),
        ('20', 'Coordinación Zona Franca'),
        ('23', 'Estudiantes en Práctica'),
        ('26', 'Preproducción Ropa Interior'),
        ('27', 'Auditoría'),
        ('28', 'Gerencia de Abastecimientos'),
    ])
    
    # Campo de carácter con opciones para el cargo.
    cargo = models.CharField(max_length=50, choices=[
        ('2', 'Director'),
        ('3', 'Gerente'),
        ('5', 'Coordinador Operativo'),
        ('6', 'Coordinador Administrativo'),
        ('7', 'Profesional'),
        ('8', 'Supervisor Operativo'),
        ('12', 'Auxiliar Operativo'),
        ('13', 'Auxiliar Administrativo'),
        ('14', 'Mecánico 1'),
        ('20', 'Operario 2'),
        ('22', 'Operario 3'),
        ('25', 'Aprendiz SENA'),
        ('26', 'Operario'),
        ('6036', 'Jefe'),
        ('60329', 'Auxiliar'),
        ('64717', 'Mecánico'),
        ('64731', 'Operario'),
        ('65131', 'Operario'),
        ('86331', 'Operario'),
    ])
    
    # Campo de carácter con opciones para el nivel.
    nivel = models.CharField(max_length=20, choices=[
        ('1', 'Alta Gerencia'),
        ('2', 'Gerencia Media 1'),
        ('3', 'Gerencia Media 2'),
        ('4', 'Nivel Supervisión'),
        ('5', 'Base Administrativa'),
        ('6', 'Base Operativa'),
        ('7', 'SENA'),
    ])
    
    # Campos de fecha para la fecha de ingreso y la fecha de retiro.
    fecha_de_ingreso = models.DateField()
    fecha_de_retiro = models.DateField(null=True, blank=True)
    
    # Campo de carácter con opciones para el motivo de retiro.
    motivo_de_retiro = models.CharField(max_length=30, choices=[
       ('Renuncia voluntaria', 'Renuncia Voluntaria'),
       ('Terminacion de contrato', 'Terminación de Contrato')
   ], null=True, blank=True)

    # Método clean para realizar validaciones personalizadas.
    def clean(self):
        # Si el estado es 'activo' y la fecha de retiro no es nula, lanza un error de validación.
        if self.estado == 'activo' and self.fecha_de_retiro is not None:
            raise ValidationError("La fecha de retiro debe ser nula cuando el estado es activo.")
        # Si el estado es 'inactivo' y la fecha de retiro es nula, lanza un error de validación.
        if self.estado == 'inactivo' and self.fecha_de_retiro is None:
            raise ValidationError("La fecha de retiro no puede ser nula cuando el estado es inactivo.")

    # Método __str__ para definir la representación en cadena del objeto.
    def __str__(self):
        return f"{self.codigo_empleado} {self.nombre}"

# Define la clase Hijo que hereda de models.Model.
class Hijo(models.Model):
    # Campo de clave foránea que referencia a informacionempleado, con relación de borrado en cascada.
    informacion_empleado = models.ForeignKey('InformacionEmpleado', related_name='hijos', on_delete=models.CASCADE)

    
    # Campos de carácter para el nombre y apellido.
    genero= models.CharField(max_length=50, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    # Campo de entero para la edad.
    fecha_de_nacimiento = models.DateField()
    @property
    def edad(self):
        today = date.today()
        return today.year - self.fecha_de_nacimiento.year - ((today.month, today.day) < (self.fecha_de_nacimiento.month, self.fecha_de_nacimiento.day))

class estudiosRealizados(models.Model):
    informacionempleado = models.ForeignKey('informacionempleado', related_name='estudios', on_delete=models.CASCADE)

    Nivel = models.CharField(null=True, blank=True, max_length=50, choices=[
        ('Basica primaria', 'Basica Primaria'),
        ('Basica secundaria', 'Basica Secundaria'),
        ('Media tecnica', 'Media Tecnica'),
        ('Tecnica', 'Tecnica'),
        ('Tecnologo', 'Tecnologo'),
        ('Profesional', 'Profesional'),
        ('Postgrado', 'Postgrado'),
        ('Maestria', 'Maestria'),

    ])
  

    Area = models.CharField(null=True, blank=True, max_length=50, choices=[
    ('Artes y diseño', 'Artes y Diseño'),
    ('Ciencias ambientales', 'Ciencias Ambientales'),
    ('Ciencias de la salud', 'Ciencias de la Salud'),
    ('Ciencias naturales y exactas', 'Ciencias Naturales y Exactas'),
    ('Ciencias sociales', 'Ciencias Sociales'),
    ('Comercio exterior', 'Comercio Exterior'),
    ('Comunicacion y periodismo', 'Comunicacion y Periodismo'),
    ('Bachiller academico', 'Bachiller Academico'),
    ('Diseño de modas', 'Diseño de Modas'),
    ('Educacion', 'Educacion'),
    ('Humanidades', 'Humanidades'),
    ('Ingenieria y tecnologia', 'Ingenieria y Tecnologia'),
    ('Mercadotecnia de moda', 'Mercado Tecnica de Moda'),
    ('Negocios y administracion', 'Negocios y Administracion'),
    ('Nutricion y dietetica', 'Nutricion y Dietetica'),
    ('Textil', 'textil'),
    ('Veterinaria', 'veterinaria'),
    
    ])

    Institucion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Nivel} en {self.Area} - {self.Institucion}"


