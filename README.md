# Aplicación Flask para sincronizar datos con una base de datos

Esta aplicación Flask proporciona un conjunto de rutas para sincronizar datos con una tabla de base de datos llamada "ambulancias" en la cual se guardan datos de un monitor de signos vitales que reporta cada segundo.

## Rutas

- `/sincronizar_datos`: Esta ruta recupera el registro más reciente con un `estado` de 0 de la tabla "ambulancias" y lo devuelve como un objeto JSON.

- `/actualizar_datos_sincronizados/<id>`: Esta ruta actualiza el `estado` del registro con el `id` especificado en la tabla "ambulancias" a 1.

- `/sincronizar_datos_faltantes/<dispositivo_id>`: Esta ruta recupera todos los registros con un `estado` de 0 y un `id` que coincida con el `dispositivo_id` especificado de la tabla "ambulancias" y los devuelve como una lista de objetos JSON.

- `/sincronizar_datos_masivos/<dispositivo_id>`: Esta ruta actualiza el `estado` de todos los registros con un `id` que coincida con el `dispositivo_id` especificado en la tabla "ambulancias" a 1.

- `/eliminar_registros/<dispositivo_id>`: Esta ruta elimina todos los registros con un `id` que coincida con el `dispositivo_id` especificado y un `estado` de 1 de la tabla "ambulancias".

## Configuración

Para ejecutar esta aplicación, deberás instalar los paquetes necesarios y configurar una base de datos MySQL.

1. Instala los paquetes necesarios:
```
pip install flask mysql-connector-python
```
2. Configura una base de datos MySQL y una tabla con la siguiente estructura:
```
CREATE TABLE ambulancias (
    _id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(15) NOT NULL,
    id VARCHAR(50) NOT NULL,
    msg VARCHAR(250) NOT NULL,
    time DATETIME NOT NULL,
    estado INT NOT NULL
);
```
3. Actualiza la variable `mydb` en el código con los detalles de conexión a MySQL.

4. Ejecuta la aplicación:
```
python nombre_archivo.py
```

## Uso

Para utilizar las rutas de esta aplicación de Flask, envía solicitudes HTTP a los puntos finales especificados utilizando el método apropiado (GET, PUT, DELETE). La respuesta será un objeto JSON o una matriz que contenga los datos devueltos por la ruta.

## Licencia

Esta aplicación está licenciada bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

# Flask App for Syncing Data with a Database

This Flask app provides a set of routes for syncing data with a database table called "ambulancias" in which data of a vital signs monitor that reports every second is saved.

## Routes

- `/sincronizar_datos`: This route retrieves the most recent record with a `status` of 0 from the "ambulancias" table and returns it as a JSON object.

- `/actualizar_datos_sincronizados/<id>`: This route updates the `status` of the record with the specified `id` in the "ambulancias" table to 1.

- `/sincronizar_datos_faltantes/<dispositivo_id>`: This route retrieves all records with a `status` of 0 and a `id` that matches the specified `dispositivo_id` from the "ambulancias" table and returns them as a list of JSON objects.

- `/sincronizar_datos_masivos/<dispositivo_id>`: This route updates the `status` of all records with a `id` that matches the specified `dispositivo_id` in the "ambulancias" table to 1.

- `/eliminar_registros/<dispositivo_id>`: This route deletes all records with a `id` that matches the specified `dispositivo_id` and a `status` of 1 from the "ambulancias" table.

## Configuration

To run this app, you will need to install the necessary packages and set up a MySQL database.

1. Install the necessary packages:
```
pip install flask mysql-connector-python
```

2. Set up a MySQL database and table with the following structure:
```
CREATE TABLE ambulancias (
    _id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(15) NOT NULL,
    id VARCHAR(50) NOT NULL,
    msg VARCHAR(250) NOT NULL,
    time DATETIME NOT NULL,
    estado INT NOT NULL
);
```

3. Update the `mydb` variable in the code with the MySQL connection details.

4. Run the app:
```
python nombre_archivo.py
```

## Usage

To use the routes in this Flask app, send HTTP requests to the specified endpoints using the appropriate method (GET, PUT, DELETE). The response will be a JSON object or an array containing the data returned by the route.

## License

This app is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


