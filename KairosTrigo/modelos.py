from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from conexion import engine


class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    categoria = Column(String)
    precio = Column(Integer)
    a_cotizar = Column(Boolean)  # True: pedido personalizado | False: Pedido del menu


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String)


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    fecha_retiro = Column(DateTime)
    tipo_entrega = Column(String)   
    direccion = Column(String)     
    estado = Column(String)         
    total = Column(Integer)
    sena = Column(Integer)              


class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    sabor = Column(String)
    porciones = Column(Integer)         
    descripcion = Column(Text)          

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tablas creadas")