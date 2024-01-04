import streamlit as st
from stockfish import Stockfish

#https://github.com/zhelyabuzhsky/stockfish/blob/master/stockfish/models.py
stockfish=Stockfish("stockfish_14_x64_avx2.exe")
stockfish.set_depth(20)#How deep the AI looks
stockfish.set_skill_level(20)#Highest rank stockfish
stockfish.get_parameters()
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

