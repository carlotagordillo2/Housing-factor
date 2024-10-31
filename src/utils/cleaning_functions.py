import pandas as pd
import re
import numpy as np

def convertir_tipo_titulo(df,columna): 
    
    df[columna] = df[columna].str.replace('-', ' ')
    df[columna] = df[columna].str.title()
    
    return df

def limpiar_localizaciones(df):
    
    df = convertir_tipo_titulo(df,'Ciudad')
    df = convertir_tipo_titulo(df, 'Zona')
    df = convertir_tipo_titulo(df, 'Barrio')
    
    
    return df

def limpiar_num(df):
    
    df['Metros cuadrados (m²)'] = df['Metros cuadrados (m²)'].str.replace('m²', '').replace('.', '').str.strip().astype(float)
    
    df['Numero habitaciones'] = df['Numero habitaciones'].str.replace('hab.', '').str.strip()
    
    return df

def cambiar_nombre_columnas(df): 
    
    df = df.rename(columns = {'Precio': 'Precio (€)', 
                    'Metros cuadrados':'Metros cuadrados (m²)'})
    
    # df = df.rename(columns = {'Precio': 'Precio (€ o €/mes)', 
    #                'Metros cuadrados':'Metros cuadrados (m²)'})
    
    return df

def division_descripcion(df):
    
    # Set columns to "Indeterminado" if "No tiene" is in the description
    no_tiene_mask = df['Descripcion'].str.lower().str.contains('no tiene', na=False)
    df.loc[no_tiene_mask, ['Planta', 'Interior/Exterior', 'Ascensor']] = 'Indeterminado'
    
    pattern = r'(?:Planta (\d+ª)|Bajo) (\w+) (?:con|sin) ascensor'

    # Extraer los componentes en nuevas columnas
    df[['Planta', 'Interior/Exterior']] = df['Descripcion'].str.extract(pattern)

    # Crear la columna 'ascensor' basada en la cadena original
    
    df['Ascensor'] = np.where(
    df['Descripcion'].str.lower().str.contains('con ascensor', na=False),'Si',df['Ascensor'])
    df['Ascensor'] = np.where(
    df['Descripcion'].str.lower().str.contains('sin ascensor', na=False),'No',df['Ascensor'])
    df['Ascensor'] = np.where(
    df['Descripcion'].str.contains('ascensor', case=False, na=False),
    np.where(df['Descripcion'].str.contains('con ascensor', case=False, na=False), 'Si', 'No'),
    'Indeterminado')
    
    df['Interior/Exterior'] = np.where(
    df['Descripcion'].str.contains('interior', case=False, na=False), 
    'Interior',
    np.where(
        df['Descripcion'].str.contains('exterior', case=False, na=False), 
        'Exterior', 
        'Indeterminado'
    ))
    #df['Ascensor'] = df['Descripcion'].str.not(contains('ascensor', na=False)).replace({True: 'Si', False: 'No'})
    #df['Interior/Exterior'] = df['Descripcion'].str.contains('exterior', na=False).replace({True: 'Exterior', False: 'Interior'})
    df['Planta'] = np.where(
    df['Descripcion'].str.lower().str.contains('bajo', na=False),'Bajo',df['Planta'])
    df['Planta'] = np.where(
    df['Descripcion'].str.lower().str.contains('sótano', na=False),'Sótano',df['Planta'])
    
    df['Planta'] = np.where(
        df['Planta'].isna(),
        df['Descripcion'].str.extract(r'(Planta \d+ª)', expand=False).fillna(df['Planta']),
        df['Planta']
    )
    df['Planta'] = np.where(
    df['Descripcion'].str.lower().str.contains('entreplanta', na=False),'Entreplanta',df['Planta'])
    
    df['Planta'] = np.where(
    df['Descripcion'].str.lower().str.contains('no tiene', na=False),'Indeterminado',df['Planta'])
    
    df['Interior/Exterior'] = np.where(
    df['Descripcion'].str.lower().str.contains('no tiene', na=False),'Indeterminado',df['Interior/Exterior'])
    
    df['Ascensor'] = np.where(
    df['Descripcion'].str.lower().str.contains('no tiene', na=False),'Indeterminado',df['Ascensor'])
    
    
    df['Planta'] = df['Planta'].fillna('Indeterminado')
    
    return df

def estimar_habitaciones(metros_cuadrados):
    if metros_cuadrados < 30:
        return 1  # Estudio o habitación pequeña
    elif metros_cuadrados < 60:
        return 2  # Apartamento pequeño
    elif metros_cuadrados < 90:
        return 3  # Apartamento de tamaño medio
    elif metros_cuadrados < 120:
        return 4  # Apartamento grande
    else:
        return 5  # Casa grande o apartamento muy espacioso
    
def no_definido_habitaciones(df):
    
    # Aplicar la estimación solo a las filas donde el número de habitaciones es 'no definido'
    df['Numero habitaciones'] = df.apply(
    lambda row: estimar_habitaciones(row['Metros cuadrados (m²)']) if row['Numero habitaciones'] == 'no definido' else row['Numero habitaciones'],
    axis=1)
    
    return df

municipios_top_20 = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia", "Palma", "Las Palmas de Gran Canaria", "Alacant/Alicante","Bilbao", "Córdoba", "Valladolid", "Vigo","L´Hospitalet de Llobregat","Gijón", "Vitoria-Gasteiz", "A Coruña", "Elche/Elx", "Granada"]


def comprobar(df_ciudades1): 
    ciudades_df = list(set(df_ciudades1['Ciudad'].to_list()))

    for ciu in ciudades_df: 
        
        if ciu not in municipios_top_20: 
            print(ciu)
            
def unificar_ciudades(df):
    
    df['Ciudad'] = df['Ciudad'].replace({
    "Gijon": "Gijón", 
    "Elche Elx": "Elche/Elx", 
    "Malaga": "Málaga", 
    "Palma De Mallorca": "Palma",
    "A Coruna": "A Coruña", 
    "Cordoba": "Córdoba", 
    "Las Palmas De Gran Canaria": "Las Palmas de Gran Canaria", 
    "Hospitalet De Llobregat": "L´Hospitalet de Llobregat", 
    "Alicante Alacant": "Alacant/Alicante", 
    "Vitoria Gasteiz": "Vitoria-Gasteiz"
})
    
    return df