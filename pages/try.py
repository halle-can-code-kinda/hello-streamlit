import requests
import streamlit as st

name = 'Michael Jordan'
api_url = 'https://api.api-ninjas.com/v1/celebrity?birthday={}'.format('1963-02-17')
response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
if response.status_code == requests.codes.ok:
    st.write(response.text)
else:
    st.write("Error:", response.status_code, response.text)