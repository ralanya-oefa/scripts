import os
import pandas as pd
import sys

# Asegurar que la consola soporte caracteres especiales
sys.stdout.reconfigure(encoding='utf-8')

def leer_rango_excel(ruta_archivo):
    try:
        # Leer el archivo Excel, comenzando en la fila 19 (índice 18), usando esa fila como encabezado
        df = pd.read_excel(
            ruta_archivo,
            usecols="B:AD",
            skiprows=18,
            header=0,
            engine='openpyxl' if ruta_archivo.endswith('xlsx') else 'xlrd'
        )

        # Extraer nombre de carpeta contenedora
        nombre_carpeta = os.path.basename(os.path.dirname(ruta_archivo))

        # Insertar columna con el nombre de la carpeta al inicio
        df.insert(0, 'Carpeta', nombre_carpeta)
        

        # Agregar nombre del archivo
        df['Archivo'] = os.path.basename(ruta_archivo)

        return df
    except Exception as e:
        print(f"⚠️ Error leyendo '{ruta_archivo}': {e}")
        return None

def consolidar_archivos_excel(directorio, salida='consolidado.xlsx'):
    archivos = []
    # Recorremos todos los subdirectorios para encontrar archivos Excel
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(('.xlsx', '.xls')):
                archivos.append(os.path.join(root, file))

    todos_dfs = []

    for ruta in archivos:
        df = leer_rango_excel(ruta)
        if df is not None:
            todos_dfs.append(df)

    if todos_dfs:
        df_consolidado = pd.concat(todos_dfs, ignore_index=True)
        df_consolidado.to_excel(salida, index=False)
        print(f"✅ Consolidado guardado como: {salida}")
    else:
        print("⚠️ No se encontraron datos válidos para consolidar.")

# 📂 Ruta base
ruta_base = r'D:\RALANYA_2025\pedido\Observaciones\Hidrocarburos'

# 🟢 Ejecutar consolidación
consolidar_archivos_excel(ruta_base)
