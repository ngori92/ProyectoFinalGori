# ProyectoFinalGori

Trabajo realizado por Nicolás Gori como proyecto final del curso de Python de CoderHouse - Camada 47770.

El trabajo simula un sitio web de una tienda online al cuál se puede acceder para ver información de los productos, empleados, proveedores y clientes de la empresa.

Al ingresar SIN CUENTA se podrá ver información básica de cada clase (solo nombre y algun datito más, foto por defecto), y en el caso de los productos también se puede ver la foto.

Al ingresar con cuenta de invitado (la que se crea el usuario a través del botón "registrarse") podemos ver, además de lo anterior:
- Fotos de los clientes, empleados, proveedores, etc.
- Acceder al botón "Ver más" que muestra un detalle completo de los ítems en cuestión.
- Avatar del usuario. Si el usuario no tiene avatar asociado, se muestra uno por defecto.

Al ingresar con cuenta registrada como del staff mediante el admin de django, se puede, además de lo anterior:
- Acceder al botón para agregar una nueva instancia de cada una de las clases (proveedor, empleado, cliente, producto..)
- Acceder al botón "Borrar" en cada una de las instancias de las clases.
- Acceder al botón "Editar" en cada una de las instancias de las clases, lo que nos permitirá modificar la información. Si probamos pegando el link del formulario de edición, el HTML tiene un IF que pide que si el usuario no está registrado como staff, no muestre el formulario, sino que muestra un mensaje pidiendo que contacte con el administrador del sitio.

Al iniciar sesión, la web de inicio nos da un mensaje de bienvenida a partir de nuestro username.
