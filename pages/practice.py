import streamlit as st

for i in range(1,100):
    if (i/5).is_integer() == True and (i/3).is_integer() == True:
        st.write("FizzBuzz")
    elif (i/3).is_integer()== True:
        st.write("Fizz")
    elif (i/5).is_integer() == True:
        st.write("Buzz")
    else:
        st.write(i)