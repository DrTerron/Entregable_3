======================================= 
IEXE Tec - Maestría en Ciencia de Datos 
=======================================

Código fuente para crear proyecto de la materia Productos de Datos - Entregable 3

Instalación
-----------

1. Descarga este repositorio:

   .. code-block:: console

       $ git clone https://github.com/IEXE-Tec/productos-de-datos.git
       $ cd productos-de-datos

2. Crea un ambiente autocontenido:

   Linux / Mac:

   .. code-block:: console

      $ python3 -m venv ~/entornos/productos_de_datos
      $ source ~/entornos/productos_de_datos/bin/activate
      $ pip install -r requirements.txt

   Puedes usar un directorio distinto a ``~/entornos``. Sólo recuerda usarlo para activar el entorno virtual,
   u omite este directorio para crear el ambiente en el directorio donde te encuentras.

   Windows:

   .. code-block:: console

      $ python3 -m venv <ruta a al directorio de ambientes>\entornos\productos_de_datos
      $ <ruta a al directorio de ambientes>\entornos\productos_de_datos\bin\activate.bat
      $ pip install -r requirements.txt

   Donde ``<ruta a al directorio de ambientes>`` es el directorio donde se va a crear el ambiente virtual,
   puedes usar otro directorio u omitirlo para crear el entorno en el directorio en el que te encuentras

3. Ubícate en alguna de las versiones dedicadas a cada entregable:

   .. code-block:: console

      $ git checkout entregable_n

   Donde ``entregable_n`` es el número de entregable:
   
   * ``entregable_2`` contiene los archivos para integrar tu modelo predictivo
   * ``entregable_3`` contiene los archivos para procesar solicitudes POST al modelo
   * ``entregable_4`` contiene los archivos para procesar solicitudes GET del histórico de predicciones
   * ``entregable_5`` contiene los archivos para actualizar una predicción mediante PUT
   * ``entregable_6`` contiene los archivos para integrar un dashboard simple

Ejecución
---------

1. Exporta la variable de entorno ``FLASK_APP``:

   Windows:

   .. code-block:: console

      $ set FLASK_APP=model_api.py

   Linux / Mac:

   .. code-block:: console

      $ export FLASK_APP=model_api.py      

2. Inicia el servidor de pruebas de Flask:

   .. code-block:: console

      $ flask run

   La salida de este comando debe ser algo así::

           * Serving Flask app "model_api.py" (lazy loading)
           * Environment: development
           * Debug mode: on
           * Restarting with stat
           * Debugger is active!
           * Debugger PIN: 216-201-467
           * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

3. Abre un navegador en http://127.0.0.1:5000/. 
   
   Si usas Cloud9 debes de abrir el firewall de AWS. Consulta los manuales de la clase para saber cómo.

*****

Finalmente, lee con cuidado los comentarios del código fuente para modificar cada entrega.
