import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title('Celulares Magazine')

requisicao = requests.get("http://localhost:5000/dados")



st.button("Tela Inicial", type="primary")
if st.button("Media, Mediana e Desvio Padrão"):
    resposta = requisicao.json()
    resposta = pd.DataFrame(resposta, index = [0])
    resposta[resposta.columns[0]] = resposta[resposta.columns[0]].round(2)
    resposta = resposta.T
    st.write(resposta)
    
    fig = px.bar(resposta, x=resposta.index, y=resposta[resposta.columns[0]])
    st.bar_chart(fig)

else:
    st.write("Tchau")



