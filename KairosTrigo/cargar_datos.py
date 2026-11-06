from sqlalchemy.orm import Session
from conexion import engine
from modelos import Producto,Cliente, Pedido, DetallePedido, DetallePersonalizado

with Session(engine) as session:
    productos = [
        Producto(nombre="Pan dulce", descripcion="Pan dulce casero, esponjoso y bien cargado.", categoria="Panes", precio=10000, unidad="c/u"),
        Producto(nombre="Rollo de canela", descripcion="Masa suave horneada con canela y baño de glaseado casero.", categoria="Dulces", precio=2500, unidad="c/u"),
        Producto(nombre="Pan de campo", descripcion="Masa de campo crocante por fuera y miga suave por dentro.", categoria="Panaderia", precio=3000, unidad="c/u"),
        Producto(nombre="Pan baguette", descripcion="Crocante, doradito y listo para acompañar tus comidas.", categoria="Panaderia", precio=1000, unidad="c/u"),
        Producto(nombre="Pan casero", descripcion="El pan de todos los días, hecho en casa.", categoria="Panederia", precio=2000, unidad="c/u"),
        Producto(nombre="Empanadas de queso", descripcion="Horneadas, con repulgue casero y bien rellenas.", categoria="Panaderia", precio=1500, unidad="c/u"),
        Producto(nombre="Rollo de queso", descripcion="Masa tierna enrollada con queso gratinado.", categoria="Panaderia", precio=2200, unidad="c/u"),

        Producto(nombre="Torta Matilda", descripcion="Bizcochuelo húmedo de chocolate con ganache intensa.", categoria="Pasteleria", precio=40000, unidad="torta"),
        Producto(nombre="Tiramisú", descripcion="vainillas embebidas en café intenso, entrelazadas con una crema de mascarpone suave y espolvoreado con cacao", categoria="Pasteleria",precio=44000, unidad="torta"),
        Producto(nombre="Cheesecake", descripcion="Base de galleta crocante, relleno suave de crema de queso y una cobertura de frutos rojos.", categoria="Pasteleria", precio=48000, unidad="torta"),
        Producto(nombre="Lemon Pie", descripcion="Masa sablée, crema de limón y merengue tostado.", categoria="Pasteleria", precio=30000, unidad="torta"),        
    ]

    session.add_all(productos)
    session.commit()

    for p in session.query(Producto).all():
        print(p.id, p.nombre, p.precio, p.unidad)