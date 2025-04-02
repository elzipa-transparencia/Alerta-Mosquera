import pandas as pd  

def analizar_contratos():  
    # Datos de ejemplo (simulando SECOP II)  
    contratos = [  
        {"id": 1, "nombre": "Contrato A", "licitacion": "Sí"},  
        {"id": 2, "nombre": "Contrato B", "licitacion": "No"}  # <- Irregularidad  
    ]  
    df = pd.DataFrame(contratos)  
    irregularidades = df[df["licitacion"] == "No"]  

    print("📊 Contratos irregulares detectados:")  
    print(irregularidades)  

if __name__ == "__main__":  
    analizar_contratos()  
