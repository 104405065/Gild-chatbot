import streamlit as st
from utils import plot_word2vec_3d

st.title("Word2Vec 3D Visualization")

user_input = st.chat_input("請在此輸入，記得一句一行")
if user_input:
    st.write("您輸入的句子是：")
    st.code(user_input)
    plot_word2vec_3d(user_input)