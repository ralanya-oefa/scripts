# pip install pandas openpyxl
import os
import pandas as pd

def listar_archivos_rstudio(directorio_base):
    # Lista donde se almacenarán los datos
    datos = []

    # Recorrer la carpeta y subcarpetas
    for ruta_raiz, carpetas, archivos in os.walk(directorio_base):
        for archivo in archivos:
            # Filtrar solo archivos con extensión .R, .Rmd, .Rproj
            if archivo.endswith(('.R', '.Rmd', '.Rproj')):
                ruta_completa = os.path.join(ruta_raiz, archivo)
                tamaño_bytes = os.path.getsize(ruta_completa)
                tamaño_mb = round(tamaño_bytes / (1024 * 1024), 2)

                # Guardar los datos en la lista
                datos.append({
                    'Nombre': archivo,
                    'Ruta': os.path.abspath(ruta_completa),
                    'Peso (MB)': tamaño_mb
                })

    return datos

def exportar_a_excel(data, archivo_salida='archivos_rstudio.xlsx'):
    # Crear un DataFrame con los datos y exportarlo a Excel
    df = pd.DataFrame(data)
    df.to_excel(archivo_salida, index=False)
    print(f'✅ Archivo Excel generado: {archivo_salida}')

# 👉 Ruta base (reemplazar por la ruta de la carpeta que quieras escanear)
directorio = 'D:/RALANYA_2025/git y gitlab repositorio/google drive/Informacion Consolidada CSEP'

# Ejecutar funciones
datos = listar_archivos_rstudio(directorio)
exportar_a_excel(datos)
