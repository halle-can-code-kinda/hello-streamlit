import streamlit as st
import random
import pandas as pd 
import chess
import chess.svg as svg
#import stchess
import base64

st.header("Fischer Random Board Generator")
#st.write("Learn more about Fischer Random [here](https://www.chess.com/terms/chess960)")

button = st.button("Generate Board")
correct = 0
if button:
    while correct == 0:
        #generate random board
        fischer_board = []
        board_setup = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        for i in range(8):
            piece = random.choice(board_setup)
            fischer_board.append(piece)
            board_setup.remove(piece)

        #check if opposite color bishops 
        even_bishop = 0
        odd_bishop = 0 
        for i in range(len(fischer_board)):
            if fischer_board[i] == "B":
                bishop_position = i
                if (bishop_position/2).is_integer() == True:
                    even_bishop = 1
                else:
                    odd_bishop = 1

        #check if king is between rooks
        rook_position = []
        king_position = 0
        rook = 0
        for i in range(len(fischer_board)):
            if fischer_board[i] == "R":
                rook_position.append(i)
            elif fischer_board[i] == "K":
                king_position = i
        
        if rook_position[0] < king_position and rook_position[1] > king_position:
            rook = 1

        #check if board is valid 
        if even_bishop == 1 and odd_bishop == 1 and rook == 1:
            correct = 1

    reverse = []
    for i in range(8):
        reverse.append(fischer_board[i].lower())

    #write to svg
    svg = ""
    for i in range(8):
        svg=svg+reverse[i]
    svg=svg+"/pppppppp/8/8/8/8/PPPPPPPP/"
    for i in range (8):
        svg=svg+fischer_board[i]
    svg = chess.Board(svg)
    #svg = chess.Board("rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    #display board
    def render_svg(svg):
        """Renders the given svg string."""
        b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
        html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
        st.write(html, unsafe_allow_html=True)

    render_svg(chess.svg.board(svg))