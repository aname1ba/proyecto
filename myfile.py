#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 

#st.title('SISMOS')
#def download_data():
url = "https://github.com/aname1ba/proyecto/blob/main/Catalogo1960_2021.csv"
#  filename = ""
#  urllib.request.urlretrieve(url,filename) 

#para gráficas de una línea
st.title('Sismos')
st.write('Analicemos los sismos')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')

