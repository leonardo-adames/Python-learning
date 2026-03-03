# Cómo usar Visual Studio Code con Python

**Visual Studio Code (`VSCode`)** es uno de los editores de código más populares del momento. Es un editor ligero, con una extensa comunidad de desarrolladores.

Una de las ventajas de VSCode es que es compatible con una gran variedad de lenguajes. Entre los que, por supuesto, se incluye Python (de hecho, es uno de los mejores entornos que podemos usar para programar en Python).

Así que vamos a ver cómo instalar y, sobre todo, cómo configurar el VSCode para el desarrollo de Python

# Instalación de Visual Studio Code

Si aún no tienes Visual Studio Code instalado en tu sistema, sigue estos pasos para descargar e instalar el editor:

    1. Abrimos el navegador web y dirígete al sitio web oficial de Visual Studio Code.

    2. Haz clic en el botón de descarga para tu sistema operativo (Windows, macOS o Linux).

    3. Una vez que se complete la descarga, ejecutamos el instalador y seguimos las instrucciones para completar la instalación.

# Configurar VSCode para Python

Para habilitar el soporte de Python en VSCode necesitamos instalar la extensión oficial de Python.

<div align="center">
<br>
    <img src="https://www.luisllamas.es/images/20438/vscode-python-extension.webp" />
</div>
<br>

Para ello,

    1. Abrimos Visual Studio Code.

    2. Vamos a la pestaña de Extensiones en la barra lateral izquierda (icono de cuatro cuadrados).

    3. En el campo de búsqueda, ponemos Python.

    4. Deberías ver la extensión “Python” ofrecida por Microsoft en los resultados de búsqueda.

    5. Haz clic en Instalar para instalar la extensión.

# Ejecución de scripts Python

Ahora ya estamos listo para crear y ejecutar un script Python en Visual Studio Code. Lo primero, resulta conveniente crear una carpeta para tu proyecto, y abrirla con VSCode.

Podéis hacerlo bien con el explorador de archivos, o con la consola de comandos haciendo

```bash
$ mkdir mi_proyecto
$ cd mi_proyecto
```

Dentro de nuestra carpeta, creamos un nuevo archivo Python haciendo clic en Archivo > Nuevo Archivo o utilizando el atajo de teclado (Ctrl + N).

Para este ejemplo podemos llamar al fichero de cualquier forma, por ejemplo, hola.py. Abrimos nuestro fichero, escribimos lo siguiente, y guardamos el fichero.

```python
print("Hola desde LuisLlamas.es")
```

Ahora, para ejecutar el script de Python podemos hacer clic en el botón de reproducción en la esquina superior derecha del editor.

<div align="center">
<br>
    <img src="https://www.luisllamas.es/images/20438/vscode-python-example.webp" />
</div>
<br>

Verás la salida de tu script en la ventana de salida de VSCode.

```
Hola desde LuisLlamas.es
```

# Cómo debuggear

Finalmente, también podemos usar Visual Studio Code para Debbugear nuestro código en Python.

Para ello con un fichero de Python abierto, hacemos clic en `Run` > `Start debugging` o utilizando el atajo de teclado (`F5`).

Nos saldrá una ventana para elegir el debugger que queremos usar. En este caso, elegimos Python Debugger.

<div align="center">
<br>
    <img src="https://www.luisllamas.es/images/20438/vscode-select-python-debugger.webp" />
</div>
<br>

A continuación, nos pedirá la configuración de Debug. De momento, elegimos `Python File`.

<div align="center">
<br>
    <img src="https://www.luisllamas.es/images/20438/vscode-select-debug-configuration.webp" />
</div>
<br>

Ahora ya podéis ejecutar línea a línea vuestro código, usar breakpoints, o usar las herramientas de debug para inspeccionar el valor de vuestras variables mientras el programa se ejecuta.


<div align="center">
<br>
    <img src="https://www.luisllamas.es/images/20438/vscode-python-debug.webp" />
</div>
<br>