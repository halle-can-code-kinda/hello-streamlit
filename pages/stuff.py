import streamlit as st
import pandas as pd

def standard_form():   
    try:
        #objective function 
        st.subheader("LP in standard form")
        sf_obj = obj_edf
        if obj_edf.iloc[0,0] == "max":
            sf_obj.iloc[0,0] = "min"
            for i in range(1,obj_edf.shape[1]):
                sf_obj.iloc[0,i] = -1*obj_edf.iloc[0,i]
        elif obj_edf.iloc[0,0] != "min":
            raise Exception

        #constraints
        c_index = 1
        c_name = " "
        sf_cons = cons_edf
        for i in range(len(sf_cons)):
            s_var = [0,0,0]
            if sf_cons.loc[i,"inequality"] == "<=":
                c_name = "s"+str(c_index)
                s_var[i] = 1
                sf_cons.insert(c_index,c_name,s_var,True)
                sf_cons.loc[i,"inequality"] = "=="
            elif sf_cons.loc[i,"inequality"] == ">=":
                c_name = "s"+str(c_index)
                s_var[i] = -1
                sf_cons.insert(c_index,c_name,s_var,True)
                sf_cons.loc[i,"inequality"] = "=="
            elif sf_cons.loc[i,"inequality"] != "==":
                raise Exception
            
            c_index = c_index+1
        st.write(sf_obj, sf_cons)
        initial_tableau(sf_obj, sf_cons)                 

    
    except:
       st.markdown(
           '''**input error**  
           objective value should be min or max  
           inequality cells should be >=, <=, or ==  
           all other cells should be numbers''')
    
def initial_tableau(obj, cons):
    st.subheader("Initial Tableau")
    new_row = pd.DataFrame({"x1": obj.iloc[0,1],"s1": 0,"s2":0,"s3":0, "inequality": "==", "RHS": "N/A"}, index=[0])
    tableau = pd.concat([new_row,cons.loc[:]]).reset_index(drop=True)
    st.write(tableau)


#initial example
st.header("LP Simplex")
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

#standard form
SF_button = st.button("Solve via Simplex Method")
if SF_button:
    standard_form()
