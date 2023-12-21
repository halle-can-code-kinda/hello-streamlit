import requests
import streamlit as st
import pandas as pd
import random


category = st.selectbox(
    'Question Category',
    ('random','language', 'sciencenature', 'general', 'fooddrink', 'peopleplaces', 'geography','historyholidays','entertainment','toysgames','music','mathematics','religionmythology','sportsleisure'))

if category == "random":
    category = random.choice(['language', 'sciencenature', 'general', 'fooddrink', 'peopleplaces', 'geography','historyholidays','entertainment','toysgames','music','mathematics','religionmythology','sportsleisure'])

if st.button("Generate Trivia Question"):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
    if response.status_code == requests.codes.ok:
        trivia = pd.DataFrame(eval(response.text))
        st.write(trivia.iloc[0,1])
        st.selectbox(' ',('Get Answer',trivia.iloc[0,2]))

    else:
        st.write("Error:", response.status_code, response.text)


