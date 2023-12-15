import streamlit as st
import pandas as pd

def stand_form():
    st.subheader("LP in standard form")
    standard_form = obj_edf
    
    try:
        if obj_edf.iloc[0,0] == "max":
            standard_form[0,0] = "min"
            standard_form.iloc[0,1] = -1*obj_edf.iloc[0,1]
        
        st.write(standard_form)
    except:
        st.write("input error")
        st.write("objective box should have min or max")
        st.write("all variable cells and RHS should have numbers")
        st.write("inequality cell should have <=, >=, or ==")


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


