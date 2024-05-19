import streamlit as st


st.title('test')

st.write('dataframe')


option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたが好きな数字は',option,'です。'