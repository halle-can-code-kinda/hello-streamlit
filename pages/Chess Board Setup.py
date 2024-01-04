import streamlit as st
import random
import chess
import base64
import chess.svg
import stockfish as sh


def create_board(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def standard():
    svg = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    create_board(chess.svg.board(svg))

def fischer_random():
    correct = 0
    while correct == 0:
        #generate random board
        white_position = []
        white_pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        for i in range(8):
            piece = random.choice(white_pieces)
            white_position.append(piece)
            white_pieces.remove(piece)

        #check if opposite color bishops 
        even_bishop = 0
        odd_bishop = 0 
        for i in range(len(white_position)):
            if white_position[i] == "B":
                bishop_position = i
                if (bishop_position/2).is_integer() == True:
                    even_bishop = 1
                else:
                    odd_bishop = 1

        #check if king is between rooks
        rook_check = []
        king_check = 0
        rook = 0
        for i in range(len(white_position)):
            if white_position[i] == "R":
                rook_check.append(i)
            elif white_position[i] == "K":
                king_check = i
        
        if rook_check[0] < king_check and rook_check[1] > king_check:
            rook = 1

        #check if board is valid 
        if even_bishop == 1 and odd_bishop == 1 and rook == 1:
            correct = 1

    black_position = []
    for i in range(8):
        black_position.append(white_position[i].lower())

    #write to svg
    svg = ""
    for i in range(8):
        svg=svg+black_position[i]
    svg=svg+"/pppppppp/8/8/8/8/PPPPPPPP/"
    for i in range (8):
        svg=svg+white_position[i]
    svg = chess.Board(svg)
    create_board(chess.svg.board(svg))
   
def transcedental():
    correct = 0
    #white position
    while correct == 0:
        #generate random board
        white_position = []
        white_pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        for i in range(8):
            piece = random.choice(white_pieces)
            white_position.append(piece)
            white_pieces.remove(piece)

        #check if opposite color bishops 
        even_bishop = 0
        odd_bishop = 0 
        for i in range(len(white_position)):
            if white_position[i] == "B":
                bishop_position = i
                if (bishop_position/2).is_integer() == True:
                    even_bishop = 1
                else:
                    odd_bishop = 1

        #check if king is between rooks
        rook_check = []
        king_check = 0
        rook = 0
        for i in range(len(white_position)):
            if white_position[i] == "R":
                rook_check.append(i)
            elif white_position[i] == "K":
                king_check = i
        
        if rook_check[0] < king_check and rook_check[1] > king_check:
            rook = 1

        #check if board is valid 
        if even_bishop == 1 and odd_bishop == 1 and rook == 1:
            correct = 1

    #black position
    correct = 0
    while correct == 0:
        #generate random board
        black_position = []
        black_pieces = ["r","n","b","q","k","b","n","r"]
        for i in range(8):
            piece = random.choice(black_pieces)
            black_position.append(piece)
            black_pieces.remove(piece)

        #check if opposite color bishops 
        even_bishop = 0
        odd_bishop = 0 
        for i in range(len(black_position)):
            if black_position[i] == "b":
                bishop_position = i
                if (bishop_position/2).is_integer() == True:
                    even_bishop = 1
                else:
                    odd_bishop = 1

        #check if king is between rooks
        rook_check = []
        king_check = 0
        rook = 0
        for i in range(len(black_position)):
            if black_position[i] == "r":
                rook_check.append(i)
            elif black_position[i] == "k":
                king_check = i
        
        if rook_check[0] < king_check and rook_check[1] > king_check:
            rook = 1

        #check if board is valid 
        if even_bishop == 1 and odd_bishop == 1 and rook == 1:
            correct = 1
    
    #write to svg
    svg = ""
    for i in range(8):
        svg=svg+black_position[i]
    svg=svg+"/pppppppp/8/8/8/8/PPPPPPPP/"
    for i in range (8):
        svg=svg+white_position[i]
    svg = chess.Board(svg)
    create_board(chess.svg.board(svg))



st.header("Chess Board Setup")
variant = st.selectbox("Chess Variant", ("Standard", "Fischer Random", "Transcedental"))
button = st.button("Generate Board")

if button:
    if variant == "Standard":
        standard()
    elif variant == "Fischer Random":
        fischer_random()
    elif variant == "Transcedental":
        transcedental()
