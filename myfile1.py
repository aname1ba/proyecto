import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib.request

#TABLA de todo los datos 
st.title('Tabla de todos los datos')
url1 = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo%20sismos%20-%20nuevo%20formato.csv'
datos1 = pd.read_csv(url1, sep=',')
st.table(datos1)


