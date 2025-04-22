# pip install pandas openpyxl

import os
import pandas as pd
from datetime import datetime

import os
import pandas as pd
from datetime import datetime

def listar_archivos_y_carpetas(ruta_base, nombre_excel="Lista_Google_Drive.xlsx"):
    datos = []

    for raiz, carpetas, archivos in os.walk(ruta_base):
        for carpeta in carpetas:
            ruta_completa = os.path.join(raiz, carpeta)
            fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).strftime('%Y-%m-%d %H:%M:%S')
            datos.append([ruta_completa, carpeta, "Carpeta", "-", "-", "-", fecha_modificacion])

        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            tamaño = os.path.getsize(ruta_completa) / 1024  # Tamaño en KB
            fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).strftime('%Y-%m-%d %H:%M:%S')
            datos.append([ruta_completa, archivo, "Archivo", f"{tamaño:.2f} KB", "-", "-", fecha_modificacion])

    # Guardar en DataFrame
    df = pd.DataFrame(datos, columns=["Ruta", "Nombre", "Tipo", "Tamaño", "ID", "URL", "Fecha de Modificación"])
    
    # Exportar a Excel
    df.to_excel(nombre_excel, index=False)
    print(f"✅ Listado guardado en {nombre_excel}")

# 📂 Ruta de la carpeta en Google Drive (ajústala según tu estructura)
# https://drive.google.com/drive/folders/1WomNqgOUewR2dmii0ZlsBtAHAIZ_iuvi?usp=drive_link
ruta_drive = "/content/drive/folders/FUENTES CSEP"
listar_archivos_y_carpetas(ruta_drive)