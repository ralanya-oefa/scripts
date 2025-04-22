import os

def listar_carpetas(ruta):
    carpetas = [nombre for nombre in os.listdir(ruta)
                if os.path.isdir(os.path.join(ruta, nombre))]
    return carpetas

# Ejemplo de uso
ruta_base = 'D:\RALANYA_2025\pedido\Observaciones'
carpetas = listar_carpetas(ruta_base)
print("Carpetas encontradas:")
for carpeta in carpetas:
    print(carpeta)