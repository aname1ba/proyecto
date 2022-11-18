#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 

#URL
url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo1960_2021.csv"
datos = pd.read_csv(url, sep=',')

#TITULO
st.title('Sismos en el Perú desde 1960 hasta el 2021 según el IGP')

#INFORMACIÓN
st.write('A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado *Cinturón de Fuego del Pacífico*, región donde la Tierra libera más del 85% de la energía acumulada en su interior debido a los procesos de convección del manto.')

st.write('En este contexto, la actividad sísmica en torno de la placa del Pacífico, es debida a los diversos procesos de convergencia de placas con velocidades de hasta 8 cm/año. En América del Sur, en su borde occidental, son las placas de Nazca y Sudamericana las que convergen y desarrollan el proceso de subducción mediante el cual, la placa oceánica de Nazca se introduce por debajo de la continental o Sudamericana. Este proceso es el causante de la geodinámica activa del país y por ende, de una importante actividad sísmica, volcánica y efectos asociados.')

#GRÁFICA FECHA VS MAGNITUD
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')
print(datos)

#GRÁFICA PROFUNDIDAD VS MAGNITUD



#MAPA
st.title('Ejemplo mapa')
df = pd.DataFrame(
    columns=['LATITUD', 'LONGITUD'])
st.map(df)

#otro mapa
st.subheader('otro mapa')
df1 = pd.DataFrame(
    np.(columns=['LATITUD', 'LONGITUD']))
st.map(df1)
