import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Modelo consumo de Urea", layout="centered"
)

in01 = st.number_input('Inserte S285ALA105')
in02 = st.number_input('Inserte S285ALA108')
in03 = st.number_input('Inserte s285ala058')
in04 = st.number_input('Inserte s285ala062 ')
in05 = st.number_input('Inserte 285FIT249.PNT')
in06 = st.number_input('Inserte S285ALA053')
in07 = st.number_input('Inserte 285FIT176B.PNT (Flujo de Urea AST)')
in08 = st.number_input('Inserte S285ALA026')
in09 = st.number_input('Inserte 285AIC131A.MEAS ')
in10 = st.number_input('Inserte 285FIT180.PNT')
in11 = st.number_input('Inserte S285ALA115')
in12 = st.number_input('Inserte 285FIT178.PNT')
in13 = st.number_input('Inserte S285ALA110')

modelo = pd.read_pickle('modelo_residual.pkl')


entradas = pd.DataFrame(columns = modelo.feature_names_in_)
entradas.loc[len(entradas)] = [in01, in02, in03, in04, in05, in06, in07, in08, in09, in10, in11, in12, in13]


predicciones = modelo.predict(entradas)
#predicciones[0]
st.write('La predicción de residual N-NH4 es: ', predicciones[0])

