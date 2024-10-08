import streamlit as st

st.write("# This works:")

if "button1" not in st.session_state:
    st.session_state["button1"] = False

if "button2" not in st.session_state:
    st.session_state["button2"] = False

if "button3" not in st.session_state:
    st.session_state["button3"] = False

if st.button("button1"):
    st.session_state["button1"] = not st.session_state["button1"]

if st.session_state["button1"]:
    if st.button("button2"):
        st.session_state["button2"] = not st.session_state["button2"]

if st.session_state["button1"] and st.session_state["button2"]:
    if st.button("button3"):
        # toggle button3 session state
        st.session_state["button3"] = not st.session_state["button3"]

if st.session_state["button3"]:
    st.write("**button3!!!**")


# Print the session state to make it easier to see what's happening
st.write(
    f"""
    ## Session state:
    {st.session_state["button1"]=}

    {st.session_state["button2"]=}

    {st.session_state["button3"]=}
    """
)