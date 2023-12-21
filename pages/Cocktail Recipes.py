import requests
import streamlit as st
import pandas as pd

st.header("Cocktail Search")
          
ingredient = st.text_input("by ingredients ('blackberry, bourbon')")


name = st.text_input("by cocktail name")

if ingredient:
    api_url = 'https://api.api-ninjas.com/v1/cocktail?ingredients={}'.format(ingredient)
    response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
    try: 
        cocktail = pd.DataFrame(eval(response.text))
        st.write(cocktail[['name', 'ingredients','instructions']])
    except:
        st.write("Error: no cocktail recipe found with all those ingredients", response.status_code, response.text)

if name:
    api_url = 'https://api.api-ninjas.com/v1/cocktail?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'VVWkroJxCJDoV5Y85g8zGQ==WO58i3UJbCn1IxvY'})
    if response.status_code == requests.codes.ok:
        cocktail = pd.DataFrame(eval(response.text))
        st.write(cocktail)
    else:
        st.write("Error: no cocktail found by this name", response.status_code, response.text)