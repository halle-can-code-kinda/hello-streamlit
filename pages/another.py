import requests
import streamlit as st
import pandas as pd

upload = st.file_uploader("Upload Goodreads CSV file", type="csv")

books = pd.read_csv(upload)
st.write(books)

