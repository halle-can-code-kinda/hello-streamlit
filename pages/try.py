import requests
import streamlit as st

name = 'Michael Jordan'
api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    st.write(response.text)
else:
    st.write("Error:", response.status_code, response.text)