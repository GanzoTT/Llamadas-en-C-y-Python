## Sistema de Llamadas con C

Este programa en C realiza las siguientes acciones:
1. Abrir un archivo
2. Leer su contenido
3. Cerrarlo
4. Hacer un fork del proceso
5. Mostrar el contenido desde el proceso padre
6. Contar sus lineas, usando la utilidad de Unix _wc_, desde el proceso hijo

## Requisitos

- Compilador de C instalado en tu sistema Linux. 
- Un archivo de texto (como `ejemplo.txt`) en el directorio donde ejecutarás el programa.
- El archivo fuente `main.c` y sus _includes_ `main.h` descargados en el mismo directorio que el archivo de texto.

## Instrucciones de Ejecución en Linux 

### 1. Crear el Archivo de Texto

Antes de ejecutar el programa, necesitas tener un archivo de texto `ejemplo.txt` en el mismo directorio que el código fuente. Puedes crearlo desde la terminal de la siguiente manera:

    echo "Este es un ejemplo de contenido dentro del archivo." > ejemplo.txt

Esto creará el archivo ejemplo.txt con el contenido "Este es un ejemplo de contenido dentro del archivo."

### 2. Compilar el progama

Con el compilador C creas el ejecutable. Por ejemplo, si tienes gcc, ejecutas el siguiente comando:

    gcc main.c -o programa

### 3. Ejecutar el programa

Ahora que tienes el ejecutable, puedes ejecutarlo de la siguiente manera:

    ./programa ejemplo.txt

i.e., le pasas como argumento cualquier archivo de texto

### 4. Salida Esperada

Si todo funciona correctamente, deberías ver algo similar en la consola:

    El contenido es:
    Este es un ejemplo de contenido dentro del archivo.

    El archivo tiene la siguiente cantidad de lineas:
    1 ejemplo.txt

## Descripción del Código

Este programa usa las siguientes llamadas al sistema:

Todo esto, utilizando las llamadas al sistema `open`, `read`, `close`, `fork` y `exec`.

    open(file, O_RDONLY): Abre el archivo en modo solo lectura. Devuelve un descriptor de archivo que es usado en las operaciones siguientes.

    read(file_descriptor, buffer, BUF_SIZE): Lee el contenido del archivo y lo pone en el arreglo `buffer`. En este caso, lee un máximo de `BUF_SIZE` bytes.

    close(file_descriptor): Cierra el archivo, liberando el descriptor de archivo y los recursos asociados.

    fork(): Hace un fork del proceso, devolviendo un PID (Process ID).

    execlp("wc", "wc", "-l", file, NULL): Reemplaza el proceso hijo con el programa de Unix `wc`, que con la bandera `-l` cuenta el número de lineas en un archivo
