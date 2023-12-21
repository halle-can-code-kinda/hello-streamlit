import requests
import streamlit as st
import pandas as pd
from datetime import datetime
  
today = datetime.now()
  
api_url = 'https://api.api-ninjas.com/v1/historicalevents?month={}&&day={}'.format(today.month,today.day)
response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
if response.status_code == requests.codes.ok:
    history = pd.DataFrame(eval(response.text))
    st.subheader("Today in History")
    for i in range(len(history)):
        st.write(history.iloc[i,0], ":", history.iloc[i,3])
else:
    st.write("Error:", response.status_code, response.text)