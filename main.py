import streamlit as st
import pandas as pd

data = {
    'Series-1':[1, 3, 4, 5, 7],
    'Series-2':[10,30,40,100,120]
}

st.title("Our First Streamlit App")
st.subheader("Introducing Streamlit in Animate Everything with Python")
st.write('''This is our first web app
Enjoy it!
''')
df = pd.DataFrame(data)
st.write(df)
st.line_chart(df)
st.area_chart(df)

my_slider = st.slider('Celsius')
st.write(my_slider, 'Celsius in Fahrenheit is ', my_slider * 9/5 + 32)