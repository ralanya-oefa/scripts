import os
import pandas as pd

def listar_contenido_recursivo(carpeta, archivo_salida="contenido.xlsx"):
    datos = []

    for ruta_actual, subdirectorios, archivos in os.walk(carpeta):
        # Agregar carpetas
        for subdirectorio in subdirectorios:
            ruta_completa = os.path.join(ruta_actual, subdirectorio)
            datos.append({"Nombre": subdirectorio, "Ruta": ruta_completa, "Tipo": "Carpeta"})

        # Agregar archivos
        for archivo in archivos:
            ruta_completa = os.path.join(ruta_actual, archivo)
            datos.append({"Nombre": archivo, "Ruta": ruta_completa, "Tipo": "Archivo"})

    # Crear un DataFrame de Pandas
    df = pd.DataFrame(datos)

    # Guardar en un archivo Excel
    df.to_excel(archivo_salida, index=False)

    print(f"Datos exportados a {archivo_salida}")

# Ruta de la carpeta a inspeccionar
carpeta = "D:/RALANYA_2025/git y gitlab repositorio/google drive/Informacion Consolidada CSEP"
listar_contenido_recursivo(carpeta)

# carpeta = "D:/RALANYA_2025/git y gitlab repositorio/google drive/Informacion Consolidada CSEP"
