import requests
import streamlit as st

text = 'roman empire'
api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    st.write(response.text)
else:
    st.write("Error:", response.status_code, response.text)