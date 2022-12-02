import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib.request

#TABLA de todo los datos 
st.title('Tabla de los sismos ocurridos en el Perú desde 1960 hasta el 2021 según el IGP')

st.write('La tabla presentada fue obtenida del siguiente [enlace](https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp)')

url = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo_sismos_nuevoformato.csv'
datos = pd.read_csv(url, sep=',')
st.table(datos)


