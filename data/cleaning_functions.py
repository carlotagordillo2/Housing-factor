import pandas as pd
import re

def convertir_tipo_titulo(df,columna): 
    
    df[columna] = df[columna].str.replace('-', ' ')
    df[columna] = df[columna].str.title()
    
    return df

def limpiar_localizaciones(df):
    
    df = convertir_tipo_titulo(df,'Ciudad')
    df = convertir_tipo_titulo(df, 'Zona')
    df = convertir_tipo_titulo(df, 'Barrio')
    
    
    return df

def cambiar_nombre_columnas(df): 
    
    df = df.rename({'Precio': 'Precio (€)', 
                    'Metros cuadrados':'Metros cuadrados (m²)'})
    
    return df