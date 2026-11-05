from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from conexion import engine


class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(Text)
    categoria = Column(String(50))
    precio = Column(Integer)
    unidad = Column(String(20))  


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    telefono = Column(String(30))


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    fecha_pedido = Column(DateTime, default=datetime.now)
    fecha_retiro = Column(Date)
    franja_horaria = Column(String(30))  # "Mañana (9 a 12 hs)", etc.
    tipo_entrega = Column(String(20))    # "retiro" o "envio"
    direccion = Column(String(200))      # solo si es envío
    estado = Column(String(20))          # "pendiente", "confirmado", etc.
    total = Column(Integer)
    sena = Column(Integer)               # monto (30% del total)
    sena_pagada = Column(Boolean)


class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    variedad = Column(String(50))        # lo que eligió (ej: pan dulce)
    precio_unitario = Column(Integer)


class DetallePersonalizado(Base):
    __tablename__ = "detalle_personalizado"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    tipo = Column(String(20))                  # "torta" u "otro"
    nombre_personalizado = Column(String(100)) # "¿Qué querés pedir?"
    cantidad = Column(Integer)
    porciones = Column(Integer)
    sabor = Column(String(50))
    descripcion = Column(Text)
    link_referencia = Column(String(300))
    imagen_por_whatsapp = Column(Boolean)
    precio_cotizado = Column(Integer)          # vacío hasta cotizar


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tablas creadas")