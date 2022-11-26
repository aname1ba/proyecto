#myfile.py
#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib.request 

#URL
url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo1960_2021.csv"
datos = pd.read_csv(url, sep=',')

#TITULO
st.title('Sismos en el Perú desde 1960 hasta el 2021 según el IGP')

#INFORMACIÓN
st.write('A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado *Cinturón de Fuego del Pacífico*, región donde la Tierra libera más del 85% de la energía acumulada en su interior debido a los procesos de convección del manto.')

st.write('En este contexto, la actividad sísmica en torno de la placa del Pacífico, es debida a los diversos procesos de convergencia de placas con velocidades de hasta 8 cm/año. En América del Sur, en su borde occidental, son las placas de Nazca y Sudamericana las que convergen y desarrollan el proceso de subducción mediante el cual, la placa oceánica de Nazca se introduce por debajo de la continental o Sudamericana. Este proceso es el causante de la geodinámica activa del país y por ende, de una importante actividad sísmica, volcánica y efectos asociados.')

#MAPA
st.subheader('Ejemplo mapa')

df_mapa=pd.read_csv('Catalogo1960_2021-lat&lon.csv')

df =  df_mapa.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})

st.map(df)

#GRÁFICA FECHA VS MAGNITUD
st.write('Gráfica 1. Magnitud de sismos desde 1960 hasta 2021 contra Fecha UTC')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')
print(datos)

st.write('Como se puede ver en la Gráfica 1, el 23 de Junio de 2001 a las 15 horas 33 minutos, ocurrio un terremoto destructor de una magnitud de 8.4 que afectó el Sur del Perú, particularmente los Departamentos de Moquegua, Tacna y Arequipa. Este sismo tuvo características importantes entre las que se destaca la complejidad de su registro y ocurrencia. El terremoto ha originado varios miles de post-sacudidas o réplicas y alcanzó una intensidad máxima de VIII. Las localidades más afectadas por el terremoto fueron las ciudades de Moquegua, Tacna, Arequipa, Valle de Tambo, Caravelí, Chuquibamba, Ilo, algunos pueblos del interior y Camaná por el efecto del Tsunami.')

#GRÁFICA HORA VS MAGNITUD
st.write('Gráfica 2. Magnitud de sismos desde 1960 hasta 2021 contra Hora UTC')
st.line_chart(data=datos, x='HORA_UTC', y='MAGNITUD')
print(datos)



#REFERENCIAS
st.subheader('Referencias')
st.write('1. Indtituto Nacional de Defensa Civil (2006) Sismos ocurridos en el Perú a través del tiempo. Compendio Estadístico de Prevención y Atención de Desastres 2006. Recuperado de: https://www.indeci.gob.pe/compend_estad/2006/7_otras_estad/7.1_sismos/7.1.4_hist_sismos.pdf')
url2= 'https://raw.githubusercontent.com/aname1ba/proyecto/main/2Catalogo1960_2021-lat%26lon%20-%20copia.csv'
datos2= pd.read_csv(url2, sep=',')
st.map(datos2)
