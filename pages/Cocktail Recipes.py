import requests
import streamlit as st
import pandas as pd

st.header("Cocktail Search")
          
name = st.text_input("by cocktail name")
ingredient = st.text_input("by ingredients ('blackberry, bourbon')")


if ingredient:
    try:
        api_url = 'https://api.api-ninjas.com/v1/cocktail?ingredients={}'.format(ingredient)
        response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
        cocktail = pd.DataFrame(eval(response.text))
        cocktail = cocktail[['name', 'ingredients','instructions']]
        st.dataframe(cocktail, hide_index= True)
    except:
        st.markdown("**Error**: no cocktail recipe found with all those ingredients")

if name:
    try:
        api_url = 'https://api.api-ninjas.com/v1/cocktail?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
        cocktail = pd.DataFrame(eval(response.text))
        cocktail = cocktail[['name', 'ingredients','instructions']]
        st.dataframe(cocktail, hide_index= True)
    except:
        st.markdown("**Error**: no cocktail found by this name", response.status_code, response.text)