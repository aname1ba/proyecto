#myfile.py

import streamlit as st
import pandas as pd
import numpy as np
import urllib.request 

st.title('SISMOS')
def download_data():
  url = "https://www.datosabiertos.gob.pe/dataset/catalogo-sismico/resource/f9629081-0721-4101-a2c2-d0622e046f8b#{}"
  filename = ""
  urllib.request.urlretrieve(url,filename) 
