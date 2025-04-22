# ===================
import os
import pandas as pd

def listar_archivos(directorio, extension):
    archivos_con_extension = []
    
    # Recorre todas las carpetas y subcarpetas
    for raiz, dirs, archivos in os.walk(directorio):
        for archivo in archivos:
            # Si el archivo tiene la extensión que buscas
            if archivo.endswith(extension):
                # Se agrega a la lista el nombre completo del archivo con su carpeta
                archivos_con_extension.append(os.path.join(raiz, archivo))
    
    return archivos_con_extension

# Función para copiar a un archivo Excel
def guardar_en_excel(archivos, archivo_excel):
    # Convertir la lista de archivos en un DataFrame de pandas
    df = pd.DataFrame(archivos, columns=["Ruta de archivo"])

    # Escribir el DataFrame a un archivo Excel
    df.to_excel(archivo_excel, index=False, engine='openpyxl')

# Ejemplo de uso
directorio = 'D:/RALANYA_2025/pedido/Observaciones/'  # Cambia esta ruta por la de tu carpeta
extension = '.xls'  # Cambia la extensión según sea necesario
archivo_excel = 'consolidado_pedido.xlsx'  # Nombre del archivo Excel donde se guardarán los resultados

# Listar archivos con la extensión especificada
archivos = listar_archivos(directorio, extension)

# Guardar los resultados en el archivo Excel
guardar_en_excel(archivos, archivo_excel)

print(f"Los archivos han sido guardados en {archivo_excel}")
