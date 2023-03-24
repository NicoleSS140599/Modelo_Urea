import pandas as pd
import streamlit as st


modelo = pd.read_pickle('modelo_urea_01.pkl')

in01 = 9.390851    # 230AIT322.PNT 
in02 = 1.438268    # 230FY499BOPP.RO01
in03 = 1.234382    # SOLIDOS_EVAP_TON_SF2.C
in04 = 6.50        # S220ALDP004
in05 = 20.977497   # 220ALCALI.PNT
in06 = 163.354462  # 220FIC161.MEAS
in07 = 3085.845459 # 240FI020A.PNT
in08 = 3085.845459 # 240FI020A.PNT
in09 = 3085.845459 # 240FI020A.PNT
in10 = 3085.845459 # 240FI020A.PNT
in11 = 3085.845459 # 240FI020A.PNT
in12 = 3085.845459 # 240FI020A.PNT
in13 = 3085.845459 # 240FI020A.PNT


entradas = pd.DataFrame(columns = modelo.feature_names_in_)
entradas.loc[len(entradas)] = [in01, in02, in03, in04, in05, in06, in07, in08, in09, in10, in11, in12, in13]


predicciones = modelo_RF.predict(entradas)
predicciones[0]
