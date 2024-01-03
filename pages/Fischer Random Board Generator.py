import streamlit as st
import pandas as pd
import random

board_setup = ["r", "n", "b", "q", "k", "b", "n", "r"]
st.write(board_setup)

fischer_board = []*8
spaces = []*8
for i in range(8):
    spaces[i] = i+1

print(spaces)
correct = 0



