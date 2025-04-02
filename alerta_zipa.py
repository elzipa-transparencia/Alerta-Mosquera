# -*- coding: utf-8 -*-
"""
Script ALERTA ZIPA - Detecta contratos irregulares en Mosquera, Colombia.
Uso: Ejecutar en Google Colab o localmente con Python 3.8+.
"""

import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(ruta_csv):
    """Carga el CSV desde Google Drive o local."""
    try:
        # Columnas esenciales para ahorrar memoria
        columnas = ["REFERENCIA", "OBJETO", "VALOR_TOTAL", "TIPO_PROCESO", "PROVEEDOR", "MUNICIPIO"]
        datos = pd.read_csv(ruta_csv, encoding="latin1", sep=";", usecols=columnas)
        print("✅ Datos cargados correctamente.")
        return datos
    except Exception as e:
        print(f"🚨 Error al cargar el archivo: {e}")
        return None

def filtrar_irregulares(datos):
    """Filtra contratos sin licitación en Mosquera."""
    try:
        # Filtro por municipio y tipo de proceso
        datos_mosquera = datos[datos["MUNICIPIO"].str.contains("MOSQUERA", na=False, case=False)]
        irregulares = datos_mosquera[~datos_mosquera["TIPO_PROCESO"].str.contains("LICITACIÓN", na=False, case=False)]
        
        print(f"\n🔍 Resultados para Mosquera:")
        print(f"- Total contratos: {len(datos_mosquera)}")
        print(f"- Contratos irregulares: {len(irregulares)}")
        
        return irregulares
    except Exception as e:
        print(f"🚨 Error al filtrar: {e}")
        return None

def generar_graficos(datos):
    """Genera gráficos de análisis."""
    try:
        # Gráfico de distribución por tipo de proceso
        datos["TIPO_PROCESO"].value_counts().plot(kind="bar", color="skyblue")
        plt.title("Distribución por Tipo de Proceso")
        plt.savefig("grafico_tipos.png")  # Guarda el gráfico
        print("\n📊 Gráfico generado: 'grafico_tipos.png'")
    except Exception as e:
        print(f"🚨 Error en gráficos: {e}")

if __name__ == "__main__":
    # Ruta al CSV (¡cambia esto por tu ruta real!)
   ruta_csv = "/content/drive/My Drive/DATOS_SECOP_MOSQUERA/SECOP_II_-_Contratos_Electr_nicos_20250402.csv"    # Para Colab
    # RUTA_CSV = "contratos_mosquera.csv"  # Para ejecución local
    
    print("\n" + "="*50)
    print("🛠️  EJECUTANDO ALERTA ZIPA v2.0")
    print("="*50 + "\n")
    
    datos = cargar_datos(RUTA_CSV)
    if datos is not None:
        irregulares = filtrar_irregulares(datos)
        if irregulares is not None:
            generar_graficos(irregulares)
            # Guarda resultados
            irregulares.to_csv("resultados_irregulares.csv", index=False)
            print("\n💾 Archivo guardado: 'resultados_irregulares.csv'")
