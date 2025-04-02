from google.colab import drive
import pandas as pd
import os

# 1. Montar Google Drive
drive.mount('/content/drive')

# 2. Ruta exacta al CSV (¡ajusta si tu Drive está en español!)
ruta_csv = "/content/drive/My Drive/DATOS/datosmosquera.csv"  # o "Mi Unidad" en vez de "My Drive"

# 3. Cargar datos
try:
    datos = pd.read_csv(ruta_csv, encoding="latin1", sep=";")
    print("✅ CSV cargado correctamente!")
    print(f"Total de registros: {len(datos)}")
    
    # Filtrar por Mosquera (si es necesario)
    datos_mosquera = datos[datos["MUNICIPIO"].str.contains("MOSQUERA", case=False, na=False)]
    print(f"Registros de Mosquera: {len(datos_mosquera)}")

except Exception as e:
    print(f"🚨 Error: {str(e)}")
    print("\n🔍 Solución: Verifica:")
    print(f"- Ruta exacta: {ruta_csv}")
    print("- Nombre del archivo (¿es 'datosmosquera.csv'?)")
    print("- Permisos del archivo (debe ser 'Cualquiera con el enlace')")
