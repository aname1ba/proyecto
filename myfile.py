#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 

#URL
url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo1960_2021.csv"
datos = pd.read_csv(url, sep=',')

#para gráficas de una línea
st.title('Sismos')
st.write('sismos')

st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')

print(datos)
