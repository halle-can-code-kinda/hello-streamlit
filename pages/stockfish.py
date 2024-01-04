import chess
import chess.engine
import streamlit as st

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
info = engine.analyse(board, chess.engine.Limit(depth=20))

# Score: PovScore(Mate(+1), WHITE)