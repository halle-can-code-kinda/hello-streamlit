import streamlit as st
import pandas as pd

def stand_form():
    st.subheader("LP in standard form")
    standard_form = obj_edf
    if obj_edf.iloc[0,0] == max:
        standard_form.iloc[0,1] = -1*obj_edf[0,1]
    elif obj_edf.iloc[0,0] != min:
        st.write("objective value needs to be min or max")

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
    SF_button = st.button("Find LP in Standard Form", on_click=disable) 


