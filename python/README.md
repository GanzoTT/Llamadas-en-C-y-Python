## Sistema de Llamadas: Leer un Archivo con Python

Este primer programa en Python consiste en uno que realiza tres llamadas al sistema operativo: abrir un archivo, leer su contenido y cerrarlo, utilizando las funciones `os.open()`, `os.read()` y `os.close()`.

## Requisitos

- Python 3 instalado en tu sistema Linux. 
- Un archivo de texto (`ejemplo.txt`) en el directorio donde ejecutarás el programa.
- El ejecutable del codigo (`leer_archivo.py`) descargado en el mismo directorio que el script.

## Instrucciones de Ejecución en Linux 

### 1. Crear el Archivo de Texto

Antes de ejecutar el programa, necesitas tener un archivo de texto llamado ejemplo.txt en el mismo directorio que el script. Puedes crearlo desde la terminal de la siguiente manera:

    echo "Este es un ejemplo de contenido dentro del archivo." > ejemplo.txt

Esto creará un archivo ejemplo.txt con el contenido "Este es un ejemplo de contenido dentro del archivo."

### 2. Ejecutar el Script

Ahora que tienes el archivo (`ejemplo.txt`) listo, puedes ejecutar el script Python de la siguiente forma:

    python3 leer_archivo.py

### 3. Salida Esperada

Si todo funciona correctamente, primero verás el contenido del archivo (`ejemplo.txt`), luego se bifurcará el proceso, y el proceso hijo ejecutará (`ls -l`) para listar los archivos del directorio. El proceso padre esperará al hijo y te informará cuando el hijo haya terminado.
  
    Contenido del archivo:
    Este es un ejemplo de contenido dentro del archivo.
    Archivo cerrado correctamente.

    Proceso padre (PID: 18402) esperando al proceso hijo (PID: 18403).

    Proceso hijo creado. Ejecutando `wc` para contar las lineas del archivo.

    1 ejemplo.txt
    Proceso hijo 22713 terminó con estado 0.

## Descripción del Código

Este programa usa las siguientes llamadas al sistema:

    os.open(ruta_archivo, os.O_RDONLY): Abre el archivo en modo solo lectura. Devuelve un descriptor de archivo que es usado en las operaciones siguientes.
    
    os.read(fd, tamaño_buffer): Lee el contenido del archivo. En este caso, lee un máximo de 1024 bytes.
    
    os.close(fd): Cierra el archivo, liberando el descriptor de archivo y los recursos asociados.
    
    os.fork(): El sistema se bifurca en dos procesos: el padre y el hijo. El valor de retorno de os.fork() es 0 para el proceso hijo y el PID (Process ID) del hijo en el proceso padre.
    El proceso hijo realiza una tarea distinta utilizando exec().
    
    os.execvp(): Reemplaza el código en el proceso hijo con una llamada al sistema externo, en este caso, el comando ls -l que lista los archivos en el directorio de trabajo actual.
    Utilizamos os.execvp() para ejecutar el comando ls con los argumentos correctos.
    
    os.wait(): En el proceso padre, usamos os.wait() para esperar a que el proceso hijo termine, y luego informamos el estado de salida del proceso hijo.

El contenido del archivo se convierte de bytes a una cadena de texto con decode('utf-8') para ser mostrado de manera legible en la consola.
