# IIC3103---jpjoublan

## Tarea 1


Para entrar a la tarea 1 hay que ingresar al link https://morning-castle-30105.herokuapp.com y luego seleccionar Tarea 1 en la barra superior
ahí estará el listado de películas a las que se puede ingresar haciendo click en el nombre. Luego, pueden hacer click sobre cualquier elemento
de la API (naves, personas, peliculas y planetas) para conocer su información. La barra de búsqueda está bajo el lista de peliculas en
la página de la Tarea 1 y solo hay que escribir y apretar "submit" para buscar, esto podría tardar un par de segundos.

### Consideración

Al momento de realizar la búsqueda en la barra, esta se demora algunos segundos. Hay veces que esta espera toma más de lo deseado y
tira un Application error, creo que se debe a la velocidad de respuesta de internet en obtener la respuesta de la API ya que en mi casa no me pasó nunca, sin embargo al probarlo con el internet de la universidad me pasó.

### Arreglo

Arreglé el tema del tiempo en el views en la función search puse dos opciones de busqueda para agilizar el tema de busqueda en la API, sin embargo con la opcion en que llamo una vez a la API (Opcion 2), solo recibo los primeros elementos de la API, no todos, porque eso es lo que retorna la API. Dejé el código de las dos opciones escrito para que chequeen el funcionamiento, sin emabrgo dejé una mezcla de las dos para que no se alente el resultado y no tire error en la búsqueda.
