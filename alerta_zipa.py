import pandas as pd  
url = "https://www.datos.gov.co/api/views/xxxx-xxxx/rows.csv"  # Enlace real de SECOP II  
datos_reales = pd.read_csv(url)  
print(datos_reales[datos_reales["licitacion"] == "No"])  
