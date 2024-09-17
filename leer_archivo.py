import os
import sys

# Ruta del archivo que vamos a leer (debes asegurarte de que el archivo exista)
ruta_archivo = 'ejemplo.txt'

# Tamaño del buffer para leer (en bytes)
tamaño_buffer = 1024

try:
    # 1. Abrir el archivo en modo lectura
    fd = os.open(ruta_archivo, os.O_RDONLY)  # Llamada al sistema: abrir archivo
    
    # 2. Leer el contenido del archivo
    contenido = os.read(fd, tamaño_buffer)   # Llamada al sistema: leer archivo
    
    # Convertir los bytes leídos a string
    contenido_str = contenido.decode('utf-8')
    print("Contenido del archivo:")
    print(contenido_str)
    
finally:
    # 3. Cerrar el archivo
    os.close(fd)                             # Llamada al sistema: cerrar archivo
    print("Archivo cerrado correctamente.")

# 4. Crear un proceso hijo usando fork
pid = os.fork()

if pid == 0:
    # Estamos en el proceso hijo
    print("\nProceso hijo creado. Ejecutando `ls` para listar archivos del directorio.\n")
    
    # 5. Reemplazar el proceso hijo con `ls -l` usando exec
    try:
        os.execvp('ls', ['ls', '-l'])  # Llamada al sistema: exec
    except FileNotFoundError:
        print("Error: no se pudo ejecutar `ls`.")
else:
    # Estamos en el proceso padre
    print(f"Proceso padre (PID: {os.getpid()}) esperando al proceso hijo (PID: {pid}).\n")
    
    # Esperamos a que el proceso hijo termine
    pid_hijo, estado = os.wait()
    print(f"Proceso hijo {pid_hijo} terminó con estado {estado}.")

