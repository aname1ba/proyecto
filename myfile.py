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

st.write('Para visualizar la tabla completa de todos los datos registrados por el IGP visita el siguiente [enlace](https://aname1ba-proyecto-myfile1-m5nrdf.streamlit.app/).')

#SUBHEADER 1
st.subheader('Presentación del Catálogo Sísmico')

#MAPA DE TODOS LOS DATOS
st.write('Los valores de ***Longitud*** y ***Latitud*** fueron ubicados en el Mapa 1 presentado a continuación:')
st.write('*Mapa 1. Sismos en el Perú desde 1960 hasta el 2021 según el IGP*')
df_mapa=pd.read_csv('Catalogo1960_2021.csv')
df =  df_mapa.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df)


#GRÁFICA FECHA VS MAGNITUD
st.write('Asimismo, la ***Magnitud*** vs ***Fecha UTC*** fueron presentados en la Gráfica 1')
st.write('*Gráfica 1. Magnitud de sismos desde 1960 hasta 2021 contra Fecha UTC*')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')
print(datos)

st.write('Como se puede ver en la Gráfica 1, el 23 de Junio de 2001 a las 15 horas 33 minutos, ocurrio un terremoto destructor de una magnitud de 8.4 que afectó el Sur del Perú, particularmente los Departamentos de Moquegua, Tacna y Arequipa. Este sismo tuvo características importantes entre las que se destaca la complejidad de su registro y ocurrencia. El terremoto ha originado varios miles de post-sacudidas o réplicas y alcanzó una intensidad máxima de VIII. Las localidades más afectadas por el terremoto fueron las ciudades de Moquegua, Tacna, Arequipa, Valle de Tambo, Caravelí, Chuquibamba, Ilo, algunos pueblos del interior y Camaná por el efecto del Tsunami.')

#SUBHEADER 2
st.subheader('Resumen del catálogo sísmico')

#RESUMEN DE DATOS
st.write('*Tabla 1. Resumen de 21 datos aleatorios*')
urlr = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/Resumen_Catalogo_Sismos1960-2021.csv'
datosr = pd.read_csv(urlr, sep=',')
st.table(datosr)


#MAPA del resumen
st.write('*Mapa 2. Resumen de 21 datos aleatorios*')
df_mapa2 = pd.read_csv('Resumen_Catalogo_Sismos1960-2021.csv')
df2 = df_mapa2.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df2)


#SUBHEADER 3
st.subheader('Casos con mayor magnitud')

#TABLA MAYOR
st.write('*Tabla 2. Los 10 valores con mayor magnitud*')
urlM = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/MAYORvalor.csv'
datosM = pd.read_csv(urlM, sep=',')
st.table(datosM)

#MAPA MAYOR
st.write('Mapa 3. Los 10 valores con mayor magnitud registrado')
df_mapa3 = pd.read_csv('MAYORvalor.csv')
df3 = df_mapa3.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df3)

#SUBHEADER 4
st.subheader('Casos con menor magnitud registrado')

#TABLA MENOR
st.write('*Tabla 3. Los 10 valores con menor magnitud*')
urlm = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/MENORvalor.csv'
datosm = pd.read_csv(urlm, sep=',')
st.table(datosm)

#MAPA MENOR
st.write('*Mapa 4. Los 10 valores con menor magnitud*')
df_mapa4 = pd.read_csv('MENORvalor.csv')
df4 = df_mapa4.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df4)



#REFERENCIAS
st.subheader('Referencias')
st.write('1. Instituto Nacional de Defensa Civil (2006) Sismos ocurridos en el Perú a través del tiempo. Compendio Estadístico de Prevención y Atención de Desastres 2006. Recuperado de: https://www.indeci.gob.pe/compend_estad/2006/7_otras_estad/7.1_sismos/7.1.4_hist_sismos.pdf')

#AUTORES
st.write('Dashboard elaborado por: Achic, S., Fernández, A. y Valle, B.')
