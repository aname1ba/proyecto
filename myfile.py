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
st.write('A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado Cinturón de Fuego del Pacífico, región donde la Tierra libera más del 85% de la energía acumulada en su interior debido a los procesos de convección del manto.')

st.subheader('Gráficas')

st.subheader('Gráficas')


st.subheader('Gráficas')

st.subheader('Gráficas')



#GRÁFICAS
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')

print(datos)
