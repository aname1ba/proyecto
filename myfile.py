#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 



#para gráficas de una línea
st.title('Sismos')
st.write('sismos')

url = "https://github.com/aname1ba/proyecto/blob/main/Catalogo1960_2021.csv"

st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')

