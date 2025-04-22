import os
import pandas as pd

def obtener_info_archivos(ruta_base):
    datos = []

    for carpeta_raiz, subcarpetas, archivos in os.walk(ruta_base):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_raiz, archivo)
            nombre = os.path.splitext(archivo)[0]
            extension = os.path.splitext(archivo)[1]
            tipo = "Archivo"
            datos.append({
                "Nombre": nombre,
                "Ruta": ruta_completa,
                "Tipo": tipo,
                "Extensión": extension
            })

        for subcarpeta in subcarpetas:
            ruta_completa = os.path.join(carpeta_raiz, subcarpeta)
            datos.append({
                "Nombre": subcarpeta,
                "Ruta": ruta_completa,
                "Tipo": "Carpeta",
                "Extensión": ""
            })

    return datos

# Ruta que quieres analizar
ruta = "D:/RALANYA_2025/git y gitlab repositorio/google drive/Informacion Consolidada CSEP"  # <-- cámbiala por tu ruta

# Obtener la información
info = obtener_info_archivos(ruta)

# Crear DataFrame y exportar a Excel
df = pd.DataFrame(info)
df.to_excel("reporte_archivos.xlsx", index=False)

print("Reporte generado con éxito: reporte_archivos.xlsx")
