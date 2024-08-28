import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import time
import yfinance as yf
import streamlit as st

st.set_page_config(
    page_title = "Pagina para Coleta"
    ,layout='centered'
    ,
)

st.header('Coleta de Ações da Bolsa de Valores')

ticker = st.text_input('Digite o ticker da ação', 'exemplo: PETR4', key = 'placeholder')
empresa = yf.Ticker(f"{ticker}.SA")
tickerDF = empresa.history(period = '1d', start = '2021-01-01', end = '2024-08-28')

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write(f'**Empresa**: {empresa.info['longName']}')
with col2:
    st.write(f'**Mercado**: {empresa.info['industryDisp']}')
with col3:
    st.write(f'**Preço Atual**: {empresa.info['currentPrice']}')

st.line_chart(tickerDF.Close)
st.bar_chart(tickerDF.Dividends)