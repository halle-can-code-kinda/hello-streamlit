import streamlit as st

st.header('encouraging messages')

rating = st.slider("how are you feeling today?", 1, 5, 1)

if st.button('yeah this feels about right'):
    if rating == 1:
        st.write("tomorrow will be a new day")
    elif rating == 2:
        st.write("better 'tude better time")
    elif rating == 3:
        st.write("it's a great day to have a great day")
    elif rating == 5:
        st.write("great days")