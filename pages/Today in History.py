import requests
import streamlit as st
import pandas as pd

month = '12'
day = '21'
api_url = 'https://api.api-ninjas.com/v1/historicalevents?month={}&&day={}'.format(month,day)
response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
if response.status_code == requests.codes.ok:
    st.write(response.text)
    history = pd.DataFrame(eval(response.text))
    st.write(history)
else:
    st.write("Error:", response.status_code, response.text)