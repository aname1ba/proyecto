#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 



#para gráficas de una línea
st.title('Sismos')
st.write('sismos')

url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo1960_2021.csv"
file = pd.read_csv(url, sep=',')

st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')

