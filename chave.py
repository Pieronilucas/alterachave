import streamlit as st
st.title(':blue[ARRUMAR CHAVES/CNPJs/CPFs]')
chave_arrumada = st.text_input('chave: ').replace('-', '').replace('/','').replace('.','').replace(' ','')
st.info(chave_arrumada)
