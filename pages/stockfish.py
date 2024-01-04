import chess
import chess.engine
import streamlit as st

# Change this if stockfish is somewhere else
engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

# The position represented in FEN
board = chess.Board("5Q2/5K1k/8/8/8/8/8/8 w - - 0 1")

# Limit our search so it doesn't run forever
info = engine.analyse(board, chess.engine.Limit(depth=20))
st.write(info)