import streamlit as st
import pandas as pd

objective = pd.DataFrame(
    [
    {"obj": "min", "x1": 1}
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

