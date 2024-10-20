import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar dados
df = pd.read_csv("pizzas.csv")

# Treinar modelo de regressão linear
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)
# Configurar Streamlit
st.title("Prevendo o valor da Pizza")
st.divider()

# Entrada do usuário
diametro = st.number_input("Digite o tamanho da pizza: ")

# Previsão do preço
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da Pizza com diâmetro de {
             diametro:.2f}cm é de R$ {preco_previsto:.2f}. ")
