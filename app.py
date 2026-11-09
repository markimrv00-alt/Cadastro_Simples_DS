import streamlit as st

#inicialiaçao das variáveis de estado
st.title("Sistema de Cadastro")

if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"

#Tela de menu

if st.session_state.pagina == "menu":
    st.title("Menu Principal")
    st.write("Escola um opçao: ")
#Tela de cadstro
#Tela de Login