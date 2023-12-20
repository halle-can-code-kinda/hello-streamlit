import requests
import streamlit as st
import pandas as pd


category = st.selectbox(
    'Question Category',
    ('all','language', 'sciencenature', 'general', 'fooddrink', 'peopleplaces', 'geography','historyholidays','entertainment','toysgames','music','mathematics','religionmythology','sportsleisure'))

if st.button("Generate Trivia Question"):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
    if response.status_code == requests.codes.ok:
        st.write(response.text)
    else:
        st.write("Error:", response.status_code, response.text)
