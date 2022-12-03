#myfile.py
#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib.request 

#URL
url = "https://raw.githubusercontent.com/aname1ba/proyecto/main/Catalogo_sismos_nuevoformato.csv"
datos = pd.read_csv(url, sep=',')

#TITULO
st.write('Dashboard elaborado por: Achic, S., Fernández, A. y Valle, B.')
st.title('Sismos en el Perú desde 1960 hasta el 2021 según el IGP')


#INFORMACIÓN
st.write('A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado *Cinturón de Fuego del Pacífico*, región donde la Tierra libera más del 85% de la energía acumulada en su interior debido a los procesos de convección del manto.')

st.write('En este contexto, la actividad sísmica en torno de la placa del Pacífico, es debida a los diversos procesos de convergencia de placas con velocidades de hasta 8 cm/año. En América del Sur, en su borde occidental, son las placas de Nazca y Sudamericana las que convergen y desarrollan el proceso de subducción mediante el cual, la placa oceánica de Nazca se introduce por debajo de la continental o Sudamericana. Este proceso es el causante de la geodinámica activa del país y por ende, de una importante actividad sísmica, volcánica y efectos asociados.')


#SUBHEADER 1: MAPA DE TODOS LOS DATOS Y GRÁFICA (FECHA VS MAGNITUD)
st.subheader('1. Presentación del Catálogo Sísmico')
st.write('Para visualizar la información completa contenida en el catálogo sísmico registrados por el IGP visita el siguiente [enlace](https://aname1ba-proyecto-myfile1-m5nrdf.streamlit.app/).')
st.write('La ***Longitud*** y ***Latitud*** obtenidas del catálogo sísmico fueron ubicados en el *Mapa 1* en donde se puede observar a grosso modo que la mayor cantidad de casos se da en aquellas zonas que se encuentran relativamente cercanas al Océano Pacífico.')

#mapa
st.write('*Mapa 1. Sismos en el Perú desde 1960 hasta el 2021 según el IGP*')
df_mapa=pd.read_csv('Catalogo_sismos_nuevoformato.csv')
df =  df_mapa.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

st.write('La ***Magnitud*** vs ***Fecha UTC*** fueron presentados en la *Gráfica 1*, en donde se visualiza con mayor facilidad la fecha con mayor y menor magnitud de sismos registrados por el IGP.')
st.write('Uno de los picos más altos de magnitud registrados fue el 23 de Junio de 2001. En esta fecha ocurrio un terremoto destructor de una magnitud de 8.4 que afectó el Sur del Perú, particularmente los Departamentos de Moquegua, Tacna y Arequipa. Este sismo tuvo características importantes entre las que se destaca la complejidad de su registro y ocurrencia. El terremoto ha originado varios miles de post-sacudidas o réplicas y alcanzó una intensidad máxima de VIII. Las localidades más afectadas por el terremoto fueron las ciudades de Moquegua, Tacna, Arequipa, Valle de Tambo, Caravelí, Chuquibamba, Ilo, algunos pueblos del interior y Camaná por el efecto del Tsunami.[^1]')

#gráfica
st.write('*Gráfica 1. Magnitud de sismos desde 1960 hasta 2021 contra Fecha UTC*')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')
print(datos)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#SUBHEADER 2: RESUMEN Y MAPA DEL CATÁLOGO
st.subheader('2. Resumen')
st.write('Desde 1960 al 2021, se juntaron 3 años consecutivos y se separaron dando un conjunto de 21 grupos. A partir de los grupos formados se tomo un valor aleatorio por grupo para la elaboración del presente resumen. Es por ello que en la Tabla 1 se puede observar que cada valor aleatorio se encuentra contenido en cierto rango de años, esto fue elaborado con el fin de tener una distribución más representativa de los valores obtenidos.')

#resumen
st.write('*Tabla 1. Resumen del Catálogo Sísmico presentados en 21 puntos escogidos al azar*')
urlr = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/Resumen_Catalogo_Sismos1960-2021.csv'
datosr = pd.read_csv(urlr, sep=',')
st.table(datosr)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#mapa
st.write('La ***Latitud*** y ***Longitud*** provenientes de la *Tabla 1* fueron presentados en el *Mapa 2*, en donde se evidencia una distribución representativa de los puntos en el mapa.')

st.write('*Mapa 2. Resumen del catálogo sísmico representado por 21 puntos escogidos al azar*')
df_mapa2 = pd.read_csv('Resumen_Catalogo_Sismos1960-2021.csv')
df2 = df_mapa2.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df2)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#SUBHEADER 3: TABLA Y MAPA DE LOS VALORES CON MAYOR MAGNITUD
st.subheader('3. Sismos con mayor magnitud')
st.write('Las ***Magnitudes*** proporcionadas por el catálogo sísmico fueron ordenadas de mayor a menor y a partir de ello se seleccionaron los 10 valores con mayor magnitud registrado. Los resultados fueron presentados en la *Tabla 2*.')

#tabla
st.write('*Tabla 2. Los 10 valores con mayor magnitud registrados en el catálogo sísmico del IGP*')
urlM = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/MAYORvalor.csv'
datosM = pd.read_csv(urlM, sep=',')
st.table(datosM)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#mapa
st.write('La ***Latitud*** y ***Longitud*** de la *Tabla 2* fueron presentados en el *Mapa 3* del cual se puede llegar a concluir que el epicentro de los sismos de mayor magnitud son más propensos a ser registrados en el Océano Pacífico.')
st.write('*Mapa 3. Los 10 valores con mayor magnitud registrado*')
df_mapa3 = pd.read_csv('MAYORvalor.csv')
df3 = df_mapa3.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df3)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#SUBHEADER 4: TABLA Y MAPA DE LOS VALORES CON MENOR MAGNITUD
st.subheader('4. Sismos con menor magnitud')
st.write('Se ordenó de menor a mayor las ***Magnitudes*** presentadas en el catálogo sísmico y se seleccionaron los 10 primeros valores para posteriormente ser presentadas en la *Tabla 3*.')

#tabla
st.write('*Tabla 3. Los 10 valores con menor magnitud registrados en el catálogo sísmico del IGP*')
urlm = 'https://raw.githubusercontent.com/aname1ba/proyecto/main/MENORvalor.csv'
datosm = pd.read_csv(urlm, sep=',')
st.table(datosm)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#mapa
st.write('La ***Latitud*** y ***Longitud*** de los datos de la *Tabla 3* fueron presentados en el *Mapa 4* del cual se puede llegar a concluir que el epicentro de los sismos de menor magnitud son más propensos a ser registrados en el sur de Perú.')
st.write('*Mapa 4. Los 10 valores con menor magnitud registrados en el catálogo sísmico del IGP*')
df_mapa4 = pd.read_csv('MENORvalor.csv')
df4 = df_mapa4.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})
st.map(df4)
st.write('Fuente: IGP (2022) *Catálogo Sismico 1960-2021*')
st.write(' ')
st.write(' ')

#SUBHEADER 5: REFERENCIAS
st.subheader('Referencias')
st.write('[1]: Instituto Nacional de Defensa Civil (2006) Sismos ocurridos en el Perú a través del tiempo. Compendio Estadístico de Prevención y Atención de Desastres 2006. Recuperado de: https://www.indeci.gob.pe/compend_estad/2006/7_otras_estad/7.1_sismos/7.1.4_hist_sismos.pdf')
st.write('[2]: Instituto Geofísico del Perú (2022) Catálogo sísmico 1960-2021. Recuperado de: https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp')

