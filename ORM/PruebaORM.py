# Sin ORM — SQL a mano (Python)
#import sqlite3
#conn = sqlite3.connect("mi_app.db")
#cursor = conn.cursor()
#cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
#id INTEGER PRIMARY KEY,
#nombre TEXT,
#email TEXT,
#activo INTEGER )  """) 
#cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana García', 'ana@mail.com', 1)")
#conn.commit();
## Escribimos el SQL nosotros
#cursor.execute("""
#SELECT id, nombre, email
#FROM usuarios
#WHERE activo = 1
#""")
#rows = cursor.fetchall()
# Convertimos filas a diccionarios a mano
#usuarios = [
#{'id': row[0], 'nombre': row[1], 'email': row[2]}
#for row in rows
#]
#print(usuarios)
#conn.close()





# --- Con ORM — SQLAlchemy (Python) ---

#from sqlalchemy import Column, Integer, String, Boolean, create_engine
#from sqlalchemy.orm import DeclarativeBase, Session
    
# 1. Definimos la clase (#class Base(DeclarativeBase):
#    passuna sola vez)
#class Base(DeclarativeBase):
#    pass

#class Usuario(Base):
#    __tablename__ = "usuarios"

#    id      = Column(Integer, primary_key=True)
#    nombre  = Column(String)
#    email   = Column(String)
#    activo  = Column(Boolean)

# 2. Consultamos como si fueran objetos Python
#engine = create_engine("sqlite:///mi_app.db")

#Base.metadata.create_all(engine)

#with Session(engine) as session:
#    usuarios = session.query(Usuario) \
#                      .filter(Usuario.activo == True) \
#                      .all()

#    for u in usuarios:
#        print(u.nombre, u.email)  # ← atributos reales, no índices


#  --------------------------------------------------------------------------------------------     


# ¿Que diferecnias encuentran en lo que les devuelven el codigo con ORM y el codigo sin ORM?
# La diferencia entre ambos codigos, esque en el que no tiene ORM devuelve un diccionario 
# dentro de una lista de esta manera: 
# [{'id': 1, 'nombre': 'Ana García', 'email': 'ana@mail.com'}]
# Mientras que el que tiene ORM, devuelve el objeto en si:
# Ana García ana@mail.com


#  --------------------------------------------------------------------------------------------


from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id      = Column(Integer, primary_key=True)
    nombre  = Column(String)
    precio   = Column(Integer)
    stock  = Column(Integer)
    categoria = Column(String)

engine = create_engine("sqlite:///mi_app.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    productos = [
        Producto(nombre = "Medialuna", precio = 300, stock = 40, categoria = "Facturas"), # por unidad
        Producto(nombre = "Tiramisu", precio = 40000, stock = 5, categoria = "Tortas"), # tortas
        Producto(nombre = "Pan Flauta", precio = 200, stock = 50, categoria = "Panaderia"), # por unidad
        Producto(nombre = "Mango", precio = 6000, stock = 10, categoria = "Frutas"), # por kilo
        Producto(nombre = "Doritos", precio = 8000, stock = 10, categoria = "Snacks"), # el grande / c/u
    ]

    session.add_all(productos)
    session.commit()

    productos = session.query(Producto).filter(Producto.precio < 500).all()

    for p in productos:
        print(p.nombre, p.precio, p.stock, p.categoria)
