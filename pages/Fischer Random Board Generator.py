import streamlit as st
import pandas as pd
import random

st.header("Fischer Random Board Generator")
st.write("Learn more about Fischer Random [here](https://www.chess.com/terms/chess960)")

button = st.button("Generate Board")
correct = 0
if button:
    while correct == 0:
        #generate random board
        fischer_board = []
        board_setup = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for i in range(8):
            piece = random.choice(board_setup)
            fischer_board.append(piece)
            board_setup.remove(piece)

        st.write(fischer_board)

        #check if opposite color bishops 
        even_bishop = 0
        odd_bishop = 0 
        for i in range(len(fischer_board)):
            if fischer_board[i] == "b":
                bishop_position = i
                if (bishop_position/2).is_integer() == True:
                    even_bishop = 1
                else:
                    odd_bishop = 1
        #TO-DO check if king is between rooks
        rook_position = []
        king_position = 0
        rook = 0
        for i in range(len(fischer_board)):
            if fischer_board[i] == "r":
                rook_position.append(i)
            elif fischer_board[i] == "k":
                king_position = i
        
        if rook_position[0] < king_position and rook_position[1] > king_position:
            rook = 1


        #TO-DO check if board is valid 
        st.write("rook", rook)
        st.write("even bishop", even_bishop)
        st.write("odd bishop", odd_bishop)
        if even_bishop == 1 and odd_bishop == 1 and rook == 1:
            correct = 1
        st.write(correct)




