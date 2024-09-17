import os

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
