import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="População livre e população escravizada", layout="wide")
st.title("📊 População livre e população escravizada")
st.write("Comparação entre população livre e população escravizada")
st.header("Tabelas")

@st.cache_data
def carregar_dados():
    df_1872 = pd.read_excel("censo_1872.xlsx", engine="calamine")

    for df, ano in [(df_2012, 2012), (df_2026, 2026)]:
        df.columns = ["UF", "Código", "Estado", "Homens", "Mulheres"]
        df["Ano"] = ano

    return pd.concat([df_2012, df_2026], ignore_index=True)


dados = carregar_dados()

st.info(
    "Atenção: estes percentuais fazem a comparação entre homens e mulher livres e escravizadas em 1872"
)

st.sidebar.header("Filtros")
add_selectbox = st.sidebar.selectbox(
    "Tabelas / gráficos",
    ("Tabelas", "Gráficos")
)