# UNIVERSIDAD ESTATAL AMAZONICA

Carrera de Tecnologias de la Informacion
Programacion Orientada a Objetos
Profesor: Mgs. Luis Antonio Llerena Ocaña
Alumno: Danny Henry Betancourt Luzon
Semana: 15

USUARIOS DEL SISTEMA
identificacion 1101234567, contraseña 1234, Danny Betancourt
identificacion 1107654321, contraseña 1234, Carlos Perez
---

# Sistema de Restaurante - restaurante_app

## De que se trata esta entrega

Esta semana se trabajo sobre el mismo proyecto de semanas anteriores, sin
reconstruir nada desde cero. La aplicacion sigue siendo la del restaurante
Sabor Lojano: login, menu lateral, gestion de productos y de usuarios, y
el fondo con el logo como marca de agua.

Lo nuevo es que la seccion de Ventas paso de ser algo que solo vivia
mientras la ventana estaba abierta, a un registro que queda guardado de
verdad en un archivo, y que ahora relaciona a un usuario con un producto
y con la fecha en la que se hizo la venta. La idea de esta semana era
justamente eso: ver como una accion en la interfaz (elegir datos y
apretar un boton) termina convirtiendose en informacion guardada, y como
esa informacion vuelve a mostrarse despues.

## Lo que cambio respecto a la semana anterior

Antes, la venta solo pedia un producto y una cantidad, y la lista de
ventas se armaba en una tabla que se vaciaba cada vez que se cerraba el
programa. Ahora la venta pide tambien un usuario (con un
ttk.Combobox, igual que el de producto), se le agrega la fecha en la que
se registro, y todo eso se guarda en datos/ventas.json. Al volver a abrir
la aplicacion, esas ventas siguen apareciendo en la tabla.

Para esto se agrego el modelo Venta (modelos/venta.py), que no existia
como archivo aparte antes, y se amplio ArchivoServicio para que tambien
sepa leer y escribir ese archivo, igual que ya hacia con productos y
usuarios.

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── fondo_marca_agua.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   ├── icons/
│   │   ├── productos.png
│   │   ├── usuarios.png
│   │   ├── ventas.png
│   │   └── salir.png
│   ├── icono_sabor_lojano.ico
│   ├── logo_sabor_lojano.jpg
│   └── marca_agua_sabor_lojano.png
├── main.py
└── README.md
```

## Como quedo organizada la venta

Venta (modelos/venta.py) guarda la identificacion del usuario, el codigo
del producto, la cantidad y la fecha. Valida que ninguno de esos datos
venga vacio y que la cantidad sea un numero entero mayor que cero.

RestauranteServicio tiene el metodo registrar_venta(), que recibe la
identificacion del usuario, el codigo del producto y la cantidad. Ahi se
revisa, en este orden: que el usuario exista, que el producto exista,
que la cantidad sea valida y que haya stock suficiente. Si todo esta
bien, arma la fecha actual, crea el objeto Venta, descuenta el stock del
producto y guarda tanto productos.json como ventas.json. Si algo falla,
lanza un error con un mensaje claro y no cambia nada.

La vista (main_view.py) solo arma los combos de usuarios y productos,
lee lo que la persona eligio, y se lo pasa al servicio. No valida reglas
de negocio ni toca los archivos json directamente, eso sigue siendo
trabajo del servicio.

## El boton y el callback

El boton Registrar venta esta declarado asi:

ttk.Button(formulario, text="Registrar venta", command=self._registrar_venta)

Se pasa la funcion sin llamarla (sin parentesis), para que Tkinter la
ejecute recien cuando se presione el boton. Adentro de _registrar_venta()
se leen los combos y el campo de cantidad, se llama a
restaurante_servicio.registrar_venta(), y segun el resultado se muestra
un mensaje de exito o de error, se limpia el campo de cantidad y se
vuelve a dibujar la tabla de ventas con lo que haya quedado guardado.

Ese es el flujo completo de esta semana: se elige la informacion en la
interfaz, se presiona el boton, el callback se ejecuta, el servicio
valida y guarda, y la interfaz se actualiza mostrando el resultado.

## Persistencia en ventas.json

Cada venta que se registra correctamente queda guardada de inmediato en
datos/ventas.json, como una lista de objetos con identificacion_usuario,
codigo_producto, cantidad y fecha. Al iniciar la aplicacion,
RestauranteServicio carga esas ventas junto con los productos y los
usuarios, asi que la tabla de Ventas muestra el historial completo desde
el primer momento, no solo lo que se registre en esa sesion.

## Iconos y logo

El menu lateral (Productos, Usuarios, Ventas, Cerrar sesion) ahora tiene
un icono junto al texto de cada boton, guardados en
assets/icons/. El logo del restaurante sigue apareciendo en la pantalla
de acceso y en el encabezado de la pantalla principal, y de fondo en
toda la ventana se ve la version tenue del mismo logo como marca de
agua.

## Usuarios de prueba

identificacion 1101234567, contraseña 1234, Danny Betancourt

identificacion 1107654321, contraseña 1234, Carlos Perez

## Productos cargados

Humitas, categoria Comida, precio 1.50, stock 15

Jugo de tomate, categoria Bebida, precio 1.50, stock 20

Repe Lojano, categoria Comida, precio 1.25, stock 30

## Como se ejecuta

Se necesita Python con Tkinter y con la libreria Pillow instalada
(pip install pillow), porque de ahi se cargan el logo, la marca de agua
y los iconos del menu.

Desde la carpeta restaurante_app se corre:

python3 main.py

Se entra con alguno de los usuarios de la tabla de arriba. Desde el menu
de la izquierda se puede ir a Productos, Usuarios o Ventas.

## Pruebas que se hicieron

Se entro con usuario y contraseña correctos y se llego a la pantalla
principal sin errores.

En la seccion Ventas se probo elegir un usuario y un producto, escribir
una cantidad valida y registrar la venta: aparecio en la tabla con su
fecha, y el stock del producto bajo la cantidad correcta.

Se reviso el archivo ventas.json y se confirmo que la venta quedo
guardada ahi con todos sus datos.

Se cerro el programa y se volvio a abrir: la venta anterior seguia
apareciendo en la tabla y el stock actualizado tambien se mantuvo.

Se probo registrar una venta con una cantidad mayor a la disponible y el
sistema la rechazo sin guardar nada ni descontar stock.

Se probo dejar el campo de cantidad vacio o con letras y el sistema
aviso del error sin cerrarse ni guardar informacion incorrecta.
