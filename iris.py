import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title("IRIS DATA")
st.text_input("USER NAME")
uploaded_file = st.file_uploader("upload file")
button = st.button("submit")
if button == True:
    df= pd.read_csv(uploaded_file)
    st.write(df)

    st.markdown("output 1")
    st.write(df.head())



    st.markdown("output 2")
    A = alt.Chart(df).mark_point(color = 'orange').encode(
    x = 'petal_length',
    y = 'sepal_length')
    st.write(A)


    st.markdown("output 3")
    fig = plt.figure()
    y=fig.add_subplot(1,1,1)
    y.scatter(df['petal_length'],df['sepal_length'])
    y.set_xlabel("petal_length")
    y.set_ylabel("sepal_length")
    st.write(fig)
