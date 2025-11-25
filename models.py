from django.db import models

# ===========================
# PROVEEDOR
# ===========================
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# ===========================
# MEDICAMENTO
# ===========================
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_caducidad = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# ===========================
# CLIENTE
# ===========================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre

# ===========================
# VENTA
# ===========================
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Venta #{self.id_venta}"

# ===========================
# DETALLE DE VENTA
# ===========================
class Detalle_Venta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle #{self.id_detalle}"

# ===========================
# EMPLEADO
# ===========================
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
