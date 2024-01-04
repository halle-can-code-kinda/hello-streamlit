import chess
import chess.engine
import streamlit as st

def stockfish_evaluation(board, time_limit = 0.01):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish_10_x64")
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    return result['score']

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
result = stockfish_evaluation(board)
st.write(result)