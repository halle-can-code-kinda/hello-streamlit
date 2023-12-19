import streamlit as st
import pandas as pd

def stand_form():
    st.subheader("LP in standard form")
    standard_form = obj_edf
    
    try:
        if obj_edf.iloc[0,0] == "max":
            standard_form.iloc[0,0] = "min"
            standard_form.iloc[0,1] = -1*obj_edf.iloc[0,1]
        elif obj_edf.iloc[0,0] != "min":
            raise Exception
        
        st.write(standard_form)
    except:
       st.markdown(
           '''**input error*  
           objective value should be min or max  
           inequality cells should be >=, <=, or =='''
       )

st.header("LP Simplex")

objective = pd.DataFrame(
    [
    {"obj": "max", "x1": 1}
])
obj_edf = st.data_editor(objective)

constraints = pd.DataFrame(
    [
       {"x1": 1, "inequality": "<=", "RHS": 4},
       {"x1": 1, "inequality": "<=", "RHS": 4},
       {"x1": 1, "inequality": "<=", "RHS": 4},
   ]
)
cons_edf = st.data_editor(constraints)
st.write("*all decision variables must be nonnegative")

SF_button = st.button("Find LP in Standard Form")
if SF_button:
    stand_form()


