import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard de Análisis de Datos")

# subir archivo
archivo = st.file_uploader("datos_limpios.csv", type=["csv"])

if archivo is not None:
    
    df = pd.read_csv(archivo)

    st.subheader("Vista de datos")
    st.write(df.head())

    st.subheader("Información del dataset")
    st.write(df.describe())

    # selector de columnas
    columna = st.selectbox("Selecciona una columna", df.columns)

    st.subheader("Histograma")
    fig, ax = plt.subplots()
    sns.histplot(df[columna], kde=True)
    st.pyplot(fig)

    st.subheader("Correlación")
    corr = df.corr(numeric_only=True)

    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    st.pyplot(fig2)