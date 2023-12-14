import streamlit as st

st.header('encouraging messages')

rating = st.slider("how are you feeling today?", 1, 5, 1)

if st.button('yeah this feels about right'):
    if rating == 3:
        st.write("it's a great day to have a great day")

        