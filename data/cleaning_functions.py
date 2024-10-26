import pandas as pd

def convertir_tipo_titulo(df,columna): 
    
    df[columna] = df[columna].replace('-', ' ')
    df[columna] = df[columna].str.title()
    
return df 