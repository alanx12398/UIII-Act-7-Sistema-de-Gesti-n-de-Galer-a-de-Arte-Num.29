from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    estilo_principal = models.CharField(max_length=100)
    sitio_web = models.CharField(max_length=255, blank=True, null=True)
    fecha_fallecimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ObraArte(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    anio_creacion = models.IntegerField()
    tecnica = models.CharField(max_length=100)
    dimensiones = models.CharField(max_length=50)
    valor_estimado = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_adquisicion = models.DateField()
    estado_conservacion = models.CharField(max_length=50)
    ubicacion_actual = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class Exposicion(models.Model):
    nombre_exposicion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    sala = models.CharField(max_length=100)
    curador = models.CharField(max_length=100)
    costo_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    num_obras_expuestas = models.IntegerField()
    tema_exposicion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_exposicion


class ObraExposicion(models.Model):
    obra = models.ForeignKey(ObraArte, on_delete=models.CASCADE)
    exposicion = models.ForeignKey(Exposicion, on_delete=models.CASCADE)
    fecha_montaje = models.DateTimeField()
    fecha_desmontaje = models.DateTimeField()
    posicion_en_sala = models.CharField(max_length=50)
    es_destacada = models.BooleanField(default=False)
    valor_asegurado_expo = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.obra} en {self.exposicion}"


class ClienteGaleria(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField()
    preferencias_arte = models.TextField()
    presupuesto_inversion = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EmpleadoGaleria(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    especialidad_arte = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class VentaObra(models.Model):
    obra = models.ForeignKey(ObraArte, on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteGaleria, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    precio_final_venta = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    empleado_venta = models.ForeignKey(EmpleadoGaleria, on_delete=models.CASCADE)
    comision_galeria = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_entrega_obra = models.DateField()

    def __str__(self):
        return f"Venta de {self.obra} a {self.cliente}"

