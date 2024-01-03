import streamlit as st
import requests as rq
import matplotlib.pyplot as plt
import chess
import chess.pgn
import chess.svg
import base64
import os


# scorebox = st.checkbox("Display Score",False)


#svg = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR")
svg = chess.Board("rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
#svg = chess.Board("r1bkqb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

render_svg(chess.svg.board(svg))

# if scorebox:
#     # Send request if scorebox is ticked
#     score = []
#     boardScore = game.board()
#     for move in moves[0:mv]:
#         r = rq.post("https://stockfish48.herokuapp.com/score",json = {"data":board.fen()})
#         res = r.json()
#         data = res['data']
#         score.append(data)
#         boardScore.push(move)



#     fig, ax = plt.subplots()
#     ax.plot(score)
#     st.sidebar.title("Score")
#     st.sidebar.write(fig)