import chess
import chess.svg
import streamlit as st

from IPython.display import SVG

board = chess.Board()
st.write(board)
SVG(chess.svg.board(board=board,size=400))  